
import os
from getpass import getpass
from urllib.parse import quote_plus

from pymongo import MongoClient

mongo_password = os.getenv("MONGO_PASSWORD")

if not mongo_password:
    mongo_password = getpass("MongoDB password: ")

mongo_password = quote_plus(mongo_password)

MONGO_URI = (
    f"mongodb://cacheboost:{mongo_password}"
    "@localhost:27017/?authSource=admin"
)

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000
)

db = client["cacheboost"]
products_collection = db["products"]
