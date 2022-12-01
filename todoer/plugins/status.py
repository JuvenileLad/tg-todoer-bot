from ..utils.db_handler import Points
from ..utils.formatter import msg_formatter 
from ..utils.ranking_system import RankingSystem
from pyrogram import filters
from ..client import app

# command handler for status
@app.on_message(filters.command("status"))
async def status(_, message):
	text = await status_window(message) #status plugin
	await app.send_message(message.chat.id, text)

async def status_window(message):
	try:
		user_data = [Points.current(message.from_user.id, 'HP'), Points.current(message.from_user.id, 'Coins'), Points.current(message.from_user.id, 'Mana') ]# get all of user's data in DB | False if user not in DB
		# user_pos = get_leaderboard() # generate leaderboard
		healthbar = Points.HealthBar(user_data[0]//10) # get the tens position in HP
		playerRank = RankingSystem(user_data[2])
		playerRank = playerRank.getRank()
		if user_data: 
			msg_content = f"**HP:** {user_data[0]}/100\n[ {healthbar} ]\n**Coins:** 💰{user_data[1]}\n**Mana:** {user_data[2]}\n**Rank:** {playerRank}"
	except: # if user not in DB
		msg_content = " Ă̴̗N̷̤͊ ̴̤̔E̶̝̊R̴̛͇R̸̗̐O̵̱̾R̸̦̀ ̶̬̃O̸̝͆C̴̛̠C̷̬͠Ȗ̷̟R̸͔̆E̸͔͛D̷͎͗ "
	text = msg_formatter(msg_content, 'STATUS', message.from_user.mention) # format the text into RPG style
	return text
