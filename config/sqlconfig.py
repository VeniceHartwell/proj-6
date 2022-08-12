import sqlalchemy as alch
import os
import dotenv

dotenv.load_dotenv()

password = os.getenv("sql_password")
dbName = "amazon_reviews"
connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)