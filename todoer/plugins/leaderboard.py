from ..utils.db_handler import get_leaderboard
from ..utils.formatter import msg_formatter 
from ..client import app
from pyrogram import filters

# command handler
@app.on_message(filters.command("leaderboard"))
async def leaderboard(_, message):
	await _leaderboard(message)

async def _leaderboard(message):
	LBdict = get_leaderboard() # user ID and total coins in desc order of coins
	user_IDs = [i for i in LBdict]
	user_coins = [LBdict[i] for i in LBdict]
	users_ls = await app.get_users(user_IDs) # fetch user object 
	text = ''''''
	rn = 10 if len(users_ls) > 10 else len(users_ls) # only the top 10 will be shown
	for n in range(rn):
		text += f"@{users_ls[n].username} : 💰{user_coins[n]}\n"
	text = msg_formatter(text, 'LEADERBOARD', f"TOTAL: {rn}")
	if len(text) < 1:
		text = "There are no users"
	await app.send_message(message.chat.id, text)
