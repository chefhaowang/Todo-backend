from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/")
    print("MongoDB is connected:", client.server_info())
except Exception as e:
    print("Error connecting to MongoDB:", e)
