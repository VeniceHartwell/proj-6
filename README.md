# Flask API Interaction & Data Handling

## Abstract
##### How does sentiment score relate to review score?
The final comparison score of ~3.3 shows users review their products at a much higher rate than they express emotionally in their reviews, or the NLP analyzer does not pick up on sentiment well enough. While users review products at a 4 or 5 star rating (out of 5), their review sentiment score rarely reaches above 50% polarity. From the NLP's analysis we can assume that reviewers lack engaging praise or critique for their products, but if we dive deeper we may instead assume that reviews are quick and to the point, without much decorative text that may influence an NLP's polarity score. Instead, reviewers opt for helpful and utilitarian words or phrases that don;t often register on an NLP's polarity scanner. In the end, if Amazon wanted to compare users' review scores to the emotional response users have to their products, Amazon should request users to leave longer reviews. This would provide users the space to leave more flowery speech for the NLP to pick up.

## Methodology
1. Gather data (amazon_reviews.csv).
2. Build an API (main.py) to store said data.
3. Define API GET and POST endpoints.
4. Implement API functions.
5. Return data to a webpage and save any necessary files (json, CSV, etc) to the local machine.

## Primary Libraries Included
• flask
• SQLalchemy
• nltk
• spacy
• textblob
• pandas
• pymysql
• config

## Using This Repo (summary)
Use the 'API Handler' file to see in-depth function calls. The links below demonstrate function results (however, they will not work without several root files, like the CSV and local API).

### Using This Repo (detail view)
1. Download this github repo.
2. Write a .env file to include your own SQL password (include this file in a new .gitignore file if you plan to upload your work).
3. Run "python main.py" in your terminal.
4. Replace the API Handler's root links with your own console's location.
5. Run the API Handler to initialize the database, test all API functions, and modify the final post function to add your own Amazon review.

### GET: Retrieve a Sample From the SQL Database
<http://127.0.0.1:5000/db/>
This function returns a sample of the SQL database because the entire database is over 10,000 reviews long.
![get_db](github_link)

### GET: Retrieve the Sentiment Score (NLP)
<http://127.0.0.1:5000/db/sentiment>
This function returns the sentiment score of a sample of reviews, and adds a sentiment score to each sampled review.
![get_db](github_link)

### GET: Retrieve all Reviews Matching a Username
<http://127.0.0.1:5000/db/<reviewername>>
Where <reviewerName> is the name you would like to search. 
This function returns every review matching the name of the reviewer provided.
![get_db](github_link)

### POST: Add a Review
<http://127.0.0.1:5000/db/addReview?reviewerName=Joe%20R.&?helpful=[1:1]&?reviewText=It%20was%20pretty%20good,%20but%20I%20expected%20more.%20I%20do%20not%20like%20the%20product&?overall=2.0&?summary=Less%20than%20expected&?reviewTime=today>"
This function adds a new review, based on the user's input criteria (see the final section of the API Handler for a detailed example), to the SQL database.
![get_db](github_link)