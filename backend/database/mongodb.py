from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)

print("Databases:", client.list_database_names())

db = client[DATABASE_NAME]

print("Current DB:", db.name)

question_collection = db[COLLECTION_NAME]

print("Current Collection:", question_collection.name)

    