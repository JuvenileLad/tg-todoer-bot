import configparser, pymongo
from pyrogram import Client
config = configparser.ConfigParser()
config.read('config.ini')

session = config['pyrogram']['session_name']
api_id = int(config['pyrogram']['api_id'])
api_hash = config['pyrogram']['api_hash']
bot_token = config['pyrogram']['bot_token']

mongodb = config['MONGODB']['url']

client = pymongo.MongoClient(host=mongodb)
mydb = client["TestDB"]
myColl = mydb["todoerTest"]

app = Client(
	session,
	api_id = api_id,
	api_hash = api_hash,
	bot_token=bot_token)

