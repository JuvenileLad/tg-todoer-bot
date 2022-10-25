import os, pymongo
from dotenv import load_dotenv
from yaml import load
load_dotenv(dotenv_path=f"{os.getcwd()}/config.env")
from pyrogram import Client

session = os.getenv('SESSION_NAME')
api_id = os.getenv('API_HASH')
api_hash = os.getenv('API_ID')
bot_token = os.getenv('BOT_TOKEN')

mongodb = os.getenv('MONGO_URL')

client = pymongo.MongoClient(host=mongodb)
mydb = client["TestDB"]
myColl = mydb["todoerTest"]

app = Client(
	session,
	api_id = api_id,
	api_hash = api_hash,
	bot_token=bot_token)

