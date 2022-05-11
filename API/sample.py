import pymongo            # Python needs a MongoDB driver to access the MongoDB database. MongoDB driver is pymongo

mdb_obj = pymongo.MongoClient("mongodb://localhost:27017/")   #mongoDB object creation and 27017 is the default port for mongoDB

mydb = mdb_obj["info"]  # name of the database is info

tab=mydb["user_info"]   # name of the collection(table in mysql) is user_info 

doc = { "_id":1,"name": "John", "address": "Highway 37" }  # here document in mongoDB is same as a record in MySQL

x = tab.insert_one(doc)

dblist = mdb_obj.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

for x in tab.find():
  print(x)