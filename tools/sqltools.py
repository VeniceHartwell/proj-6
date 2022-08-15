from config.sqlconfig import engine

# GET
def add_review (reviewerName, helpful, reviewText, overall, summary, reviewTime):
    engine.execute(f"""
        INSERT INTO reviews (reviewerID, asin, reviewerName, helpful, reviewText, overall, summary, unixReviewTime, reviewTime)
        VALUES (NULL, NULL, '{reviewerName}', '{helpful}', '{reviewText}', '{overall}', '{summary}', NULL, '{reviewTime}');
        """)
    
    return f"Correctly introduced: {reviewerName} {helpful} {reviewText} {overall} {summary} {reviewTime}"