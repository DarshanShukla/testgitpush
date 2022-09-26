import pymongo
client = pymongo.MongoClient("mongodb+srv://darshan:Datascience#2023@cluster0.cfokdce.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"darshan",
    "email":"darshanshukla28@gmail.com",
    "surname":"shukla"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )