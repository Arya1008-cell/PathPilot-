from pymongo import MongoClient

client = MongoClient("mongodb+srv://aryachandankhede_db_user:ifzDvcnsLXO2qkUV@cluster0.9lfu32j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["career_db"]
collection = db["results"]
