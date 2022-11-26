from pymongo import MongoClient

from datetime import datetime
from dotenv import dotenv_values

dotenv = dotenv_values(".env")

print(dotenv)

DATABASE = MongoClient(dotenv['MONGO_URI'])[dotenv['DB_NAME']]

client = MongoClient('localhost', 27017)
