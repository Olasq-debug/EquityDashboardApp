from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://olalekan:fatokun1234@cluster0.eormjy1.mongodb.net/?retryWrites=true&w=majority"

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
                          
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("pinging:", e)

mydb = client["equityDatabase"]
myCollection = mydb["AccountInfo"]
if myCollection in mydb.list_collection_names():
    print("Collection exist")
