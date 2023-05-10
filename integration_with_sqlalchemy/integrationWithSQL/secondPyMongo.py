import pymongo as pyM
import pprint


client = pyM.MongoClient("mongodb+srv://leandrotrombini:mqAjuE7nLp9UdkBA@cluster0.d56re2e.mongodb.net/?retryWrites=true&w=majority")

db = client.test 
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({"author":"Leandro"}))

print("\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pyM.ASCENDING)], unique=True)




print("\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
print(sorted(list(db.profiles.index_information())))



print("\n\n\n##############################################\n")
user_profile_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Mary'}
]

# result = db.profile_user.insert_many(user_profile_user)

print(db.list_collection_names())
print(posts.delete_one({"author": "Mike"}))
