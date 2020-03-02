from pymongo import MongoClient

# It will connect to default Host and Port to MongoDB
#client = MongoClient('localhost', 27017)

# Using MongoURL
#client = MongoClient('mongodb://localhost:27017')

my_client = MongoClient()
db = my_client.mydb # Accessing a Database
users = db.users # Creating a Collection (table)
user1 = {'username':'Nick', 'password':'password', 'favorite_number':445, 'hobbies':['Python', 'Games', 'Pizza']}
user2 = {'username':'Prash', 'password':'password', 'favorite_number':617, 'hobbies':['Python', 'Games', 'Pizza']}

# Inserting a Document inside MongoDB database
# user_id = users.insert_one(user1).inserted_id
# print(user_id)

# Bulk Inserts
# users_list = [
#     {'username':'Name3', 'password':'password', 'favorite_number':81, 'hobbies':['Python', 'Games', 'Hello']},
#     {'username':'Ketaki', 'password':'password', 'favorite_number':5712, 'hobbies':['Python', 'Games', 'Pizza']}]
#
# inserted = users.insert_many(users_list)
# print(inserted.inserted_ids)

# Counting Documents - Rows in a Table
print(users.count_documents({}))
print(users.count_documents({'favorite_number': 81, 'username':'Name3'}))
