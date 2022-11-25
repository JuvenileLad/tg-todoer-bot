import os, pymongo
from dotenv import load_dotenv
load_dotenv(dotenv_path=f"{os.getcwd()}/config.env")
from pyrogram import Client

version = float(os.getenv('VERSION'))
session = os.getenv('SESSION_NAME')
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

mongodb = os.getenv('DATABASE_URL')

client = pymongo.MongoClient(host=mongodb)
mydb = client["TestDB"]
myColl = mydb["todoerTest"]

app = Client(
	session,
	api_id = api_id,
	api_hash = api_hash,
	bot_token=bot_token)

