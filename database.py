import pymongo
DEFAULT_CONNECTION_URL="mongodb+srv://bike:bikepassword@cluster0.wppk4.mongodb.net/bikedb?retryWrites=true&w=majority"
client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
print(client)
print("Connection establish")

 #creating DB
db_name = "bikedb"
database = client[db_name]
print("DB created!!")

 #creating collection
collection_name = "bikecollection"
collection = database[collection_name]
print("collection Created!!")

count = 5
while True:

    print("Current value of count: ", count)
    count += 1

data={
    '_id':2,
    'companyName': a,
     'product': b,
     'courseOffered': c
}
collection.insert_one(data)
print("data inserted!!")