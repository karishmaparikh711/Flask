from flask import Flask
from flask_pymongo import pymongo
from application import app, routes
CONNECTION_STRING = "mongodb+srv://user:Tcs1234@tcs-hms-7n83z.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db1 = client.get_database('tcs_hms')
user_collection = pymongo.collection.Collection(db1, 'user_collection')