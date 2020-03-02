import pymongo
from pymongo import MongoClient

my_client = MongoClient()
db = my_client.mydb # Accessing a Database
users = db.users # Creating a Collection (table)

# Creating an Index

# print(users.create_index([('username', pymongo.ASCENDING)], unique = True))
print(users.create_index([('username', pymongo.ASCENDING)]))