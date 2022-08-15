# Data Handling & Flask API Interaction Project

## Methodology
1. Gather data (amazon_reviews.csv).
2. Build an API (main.py) to store said data.
3. Define and implement API GET functions.
4. Define and implement API POST functions.
5. Return any necessary files (json, CSV, etc).

## Hypothesis & Analysis
##### How does sentiment score relate to review score?
The final comparison score of ~3.3 shows users review their products at a much higher rate than they express emotionally in their reviews, or the NLP analyzer does not pick up on sentiment well enough. While users review products at a 4 or 5 star rating (out of 5), their review sentiment score rarely reaches above 50% polarity. From the NLP's analysis we can assume that reviewers lack engaging praise or critique for their products, but if we dive deeper we may instead assume that reviews are quick and to the point, without much decorative text that may influence an NLP's polarity score. Instead, reviewers opt for helpful and utilitarian words or phrases that don;t often register on an NLP's polarity scanner. In the end, if Amazon wanted to compare users' review scores to the emotional response users have to their products, Amazon should request users to leave longer reviews. This would provide users the space to leave more flowery speech for the NLP to pick up.

## Main Libraries Used
• flask
• SQLalchemy
• nltk
• spacy
• textblob
• pandas
• pymysql
• config

## File Functions
Use the 'API Handler' file to see in-depth function calls. The links below demonstrate function results (however, they will not work without several root files, like the CSV and local API).

### GET: Test the Database
<requests.get("http://127.0.0.1:5000/db").json()>
This function ...

### GET: Retrieve the Sentiment Score (NLP)
<http://127.0.0.1:5000/db/sentiment>
This function ...

### GET: ???
<requests.get("http://127.0.0.1:5000/db").json()>
This function ...

### POST: Add a Review
<requests.get("http://127.0.0.1:5000/db").json()>
This function ...