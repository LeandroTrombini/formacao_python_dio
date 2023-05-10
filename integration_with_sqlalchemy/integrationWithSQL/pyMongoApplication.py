import pymongo as pyM
import datetime
import pprint

client = pyM.MongoClient("mongodb+srv://leandrotrombini:mqAjuE7nLp9UdkBA@cluster0.d56re2e.mongodb.net/?retryWrites=true&w=majority")

db = client.test 
collection = db.test_collection

print("\n----------Test collection----------\n")
print(db.test_collection)

post = {
    "author": "Mike",
    "text": "My first mongodb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

print("\n----------Post id----------\n")
print(post_id)

print("\n----------List collection names----------\n")
print(db.list_collection_names())

print("\n----------Find one post----------\n")
print(db.posts.find_one())

print("\n----------Find one post FORMATED----------\n")
pprint.pprint(db.posts.find_one())

# bulk inserts

new_posts = [{
    "author": "Ana",
    "text": "Another post",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.utcnow()
}, 
{
    "author": "Leandro",
    "text": "Another post, again",
    "tags": ["bulk2", "post2", "insert2"],
    "date": datetime.datetime.utcnow()
}]


result = posts.insert_many(new_posts).inserted_ids

print("\n----------Find one post FORMATED----------\n")
pprint.pprint(db.posts.find_one({"author": "Ana"}))

print("\n----------Documents in posts collection----------\n")
for post in posts.find():
    pprint.pprint(post)