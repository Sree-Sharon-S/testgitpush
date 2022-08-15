import pymongo

client = pymongo.MongoClient("mongodb+srv://Sharon:Sreesharon97*@sreesha.0ubo3iq.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "sha",
    "mail": "sha@gmail.com",
    "surname":"siv"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)