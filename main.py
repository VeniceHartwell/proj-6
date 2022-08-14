# libraries for API
from flask import Flask
import random
from flask import jsonify

# libraries for NLP
#from nltk.corpus import stopwords
import spacy
from textblob import TextBlob
from statistics import mean

# libraries to access SQL
import pymysql
import pandas as pd
from config.sqlconfig import engine


# init flask
app = Flask(__name__)


# flask test
@app.route("/")
def greeting ():
    return f"Test successful"


# display original database
@app.route("/db")
def database():
    
    df = pd.read_sql_query(
    """
    SELECT reviewerName, helpful, reviewText, overall, summary, reviewTime FROM reviews ORDER BY helpful DESC LIMIT 100;
    """, engine)
    
    return str(df)


# display all reviews from the database matching the given name
@app.route("/db/{reviewerName}") # FIX: HOW TO WRITE PARAM?
def database():
    
    df = pd.read_sql_query( # FIX: HOW TO WRITE PARAM?
    """
    SELECT reviewerName, helpful, reviewText, overall, summary FROM reviews WHERE reviewerName == reviewerName ORDER BY helpful DESC LIMIT 100;
    """, engine)
    
    return str(df)


# display database with added sentiment score, using NLP on review text
@app.route("/db/sentiment")
def sentiment():

    # SQL -> DF
    df = pd.read_sql_query(
    """
    SELECT reviewerName, helpful, reviewText, overall, summary FROM reviews ORDER BY helpful DESC LIMIT 100;
    """, engine)

    # init vars to use in function
    word_list = []
    sentiment_ready = []
    lemmatized = []
    nlp = spacy.load("en_core_web_sm")
    stop = nlp.Defaults.stop_words # all stop words, for removing stop words from reviews

    # find the sentiment of each review
    for review in df['reviewText']: # for every review
        review_to_split = review
        for word in review_to_split.split(" "): # for every word in selected review
            if word not in stop:
                word_list.append(word)  # add split words from each review into a list of words (word_list)

        string_without_stop = " ".join(word_list) # turn back into a string
        tokens = nlp(string_without_stop) # tokenize each review

        for token in tokens:
            lemmatized.append(token.lemma_) # lemmatize each review
        sentiment_ready.append(TextBlob(" ".join(lemmatized)).sentiment.polarity) #store the sentiment of each review in a list

    # compare to overall (overall-sentiment*5) & add to df
    sentiment_comparison = []
    for index, rows in df.iterrows():
        # print(rows['overall'], sentiment_ready[index]) # a test print, to visualize the difference before outputing a sum
        sentiment_comparison.append(rows['overall']-sentiment_ready[index]*5) # original review score (out of 5) - new score from NLP analysis of review

    # store comparison and new value back into df for later visualization
    dict_to_merge = {'sentiment polarity':sentiment_ready, 
                    'sentiment comparison':sentiment_comparison} # Add all lists to a new (temp) dataframe.

    # concatenate dataframes
    df2 = pd.DataFrame(dict_to_merge)
    df_new = pd.concat([df, df2], axis=1)

    # export df to new csv
    df_new.to_csv('output/amazon_review_sentiment.csv', index="False")

    print('average difference between user\'s review score (out of 5) vs review sentiment score: ',
        mean(sentiment_comparison))
    return str(df_new.head())


# display database with new review added
@app.route("/db/sentiment")
def sentiment(): # FIX: ADD PARAMS OR DATA HERE?
    
    # SQL -> DF
    df = pd.read_sql_query(
    """
    SELECT reviewerName, helpful, reviewText, overall, summary, reviewTime FROM reviews ORDER BY helpful DESC;
    """, engine)

    # add new review to df
    dict_to_merge = {"reviewerName":reviewerName, "helpful":helpful, 
        "reviewText":reviewText, "overall":overall, "summary":summary} # add review to new dict
    df2 = pd.DataFrame(dict_to_merge) # translate dict to df
    df_new = pd.concat([df, df2], axis=1) # concatenate dataframes
    return str(df.tail()) #display df with new review


# run the flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)


'''
# References from previous project

@app.route("/line/<name>")
def all_from_mongo (name):
    lines = mongo.all_sentences(name)
    return jsonify(lines)

@app.route("/database")
def database():
    
    myclient = MongoClient("mongodb://localhost:27017/")
    #mongoclient
    
    mydb = myclient["Ironhack"]
    mycol = mydb["amazon_reviews"]
    #database and coll
    
    return str(mycol.find_one())
'''
