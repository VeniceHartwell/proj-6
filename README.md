# Data Handling & Flask API Interaction Project

## Methodology
1. Gather data (amazon_reviews.csv)
2. Build an API (main.py)
3. Define which endpoints (API instructions) to use
4. Implement the actions those endpoints will do. Examples include:
   • descriptive metrics for the data
   • sentiment analysis on text
   • word frequency
   • length of texts
   • check the SA of reviews of bookings in different years
   • generate gaphs and save them (not rendered)
   • email generated 'reports' based on endpoints
5. Return json file(s)

## Hypothesis & Analysis
##### How does sentiment score relate to review score (out of 5)?
The final comparison score of ~3.3 shows users review their products at a much higher rate than they express emotionally in their reviews, or the NLP analyzer does not pick up on sentiment well enough. While users review products at a 4 or 5 star rating (out of 5), their review sentiment score rarely reaches above 50% polarity. From the NLP's analysis we can assume that reviewers lack engaging praise or critique for their products, but if we dive deeper we may instead assume that reviews are quick and to the point, without much decorative text that may influence an NLP's polarity score. Instead, reviewers opt for helpful and utilitarian words or phrases that don;t often register on an NLP's polarity scanner. In the end, if Amazon wanted to compare users' review scores to the emotional response users have to their products, Amazon should request users to leave longer reviews. This would provide users the space to leave more flowery speech for the NLP to pick up.

## Resources
• Libraries: flask, SQLalchemy, nltk, spacy, textblob, pandas, pymysql, config