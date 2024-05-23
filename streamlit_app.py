
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit
import pprint

uri = "mongodb+srv://ryanwalter12:IDEEzWF3n5Tz02o0@cluster0.i3rreu4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.sample_mflix
x = db.list_collection_names()


st.write(x)
