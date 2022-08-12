# libraries for API
from flask import Flask
import random
from flask import jsonify

#import tools.mongotools as mongo
# mongo.all_sentences()

# libraries to access SQL
import pymysql
import pandas as pd
from config.sqlconfig import engine

app = Flask(__name__)

@app.route("/")
def greeting ():
    return f"Test successful"

@app.route("/db")
def database():
    
    df = pd.read_sql_query(
    """
    SELECT reviewerName, helpful, reviewText, overall, summary, reviewTime FROM reviews ORDER BY helpful DESC;
    """, engine)
    
    return str(df)

@app.route("/db/sentiment")
def sentiment():
    
    # SQL -> DF
    df = pd.read_sql_query(
    """
    SELECT reviewerName, helpful, reviewText, overall, summary, reviewTime FROM reviews ORDER BY helpful DESC;
    """, engine)

    # NLP: sentiment of reviewText
    sentiment_score = []
    for index in df['reviewText']:
        sentiment_score.append(???????)
    
    # compare to overall (overall-sentiment*5) & add to df
    sentiment_comparison = []
    for index, rows in df.itterows():
        sentiment_comparison.append(rows['overall']-sentiment_score[index]*5)
    
    for elem in df:
        sentiment_comparison.append(elem['overall']-sentiment_score[elem]*5)
    
    return avg(sentiment_comparison)

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
