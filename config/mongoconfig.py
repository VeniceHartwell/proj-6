from pymongo import MongoClient
import dotenv
import os

dotenv.load_dotenv()

dburl = os.getenv("URL")

if not dburl:
    raise ValueError("No URL for database")

client = MongoClient()
db = client.get_database("Ironhack")
c = db["amazon_reviews"]