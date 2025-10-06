from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId
import os

app = FastAPI()

# --- MongoDB connection ---
MONGO_USER = os.getenv("MONGO_INITDB_ROOT_USERNAME", "root")
MONGO_PASS = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "example")
MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")

MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin"

client = MongoClient(MONGO_URL)
db = client["news"]

# --- Helper to serialize MongoDB docs ---
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@app.get("/items/{collection}")
def get_items(collection: str):
    """Return all documents from the given collection in the 'news' database."""
    if collection not in db.list_collection_names():
        raise HTTPException(status_code=404, detail=f"Collection '{collection}' not found")

    col = db[collection]
    docs = list(col.find())
    return [serialize_doc(doc) for doc in docs]
