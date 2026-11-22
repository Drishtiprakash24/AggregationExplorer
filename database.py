
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# MongoDB connection URL
MONGO_URI = "mongodb://localhost:27017/"

try:
    # Connect to MongoDB
    client = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=5000
    )

    # Verify connection
    client.admin.command("ping")

    print("MongoDB connected successfully!")

    # Select database
    db = client["AggregationExplorer"]

    # Select users collection
    users_collection = db["users"]

except ConnectionFailure as e:
    print("MongoDB connection failed:", e)
