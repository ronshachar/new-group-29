from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user_for_web_project:password_for_web_project@cluster0.gst2cah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['db_for_web_project']
for collection in db.list_collection_names():
    print('collection : ' + collection)
    print()
    for i in list(db[collection].find()):
        print(i)
