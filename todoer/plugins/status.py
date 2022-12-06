from ..utils.db_handler import Points
from ..utils.formatter import msg_formatter 
from ..utils.ranking_system import RankingSystem
from pyrogram import filters
from ..client import app
from PIL import Image, ImageDraw, ImageFont
import os
# init fonts
font = ImageFont.truetype(f'{os.getcwd()}/todoer/utils/resources/Kalam-Bold.ttf', 60)
subfont = ImageFont.truetype(f'{os.getcwd()}/todoer/utils/resources/Kalam-Bold.ttf', 50)
hebrew_font = ImageFont.truetype(f'{os.getcwd()}/todoer/utils/resources/Heb.otf', 100)

# command handler for status
@app.on_message(filters.command("status"))
async def status(_, message):
	user_data = await status_window(message) #status plugin
	await status_image(user_data, message.from_user.first_name)
	await app.send_photo(message.from_user.id, photo=f'{os.getcwd()}/todoer/utils/resources/new_status.png', caption='__Devil-In-The-Slot-666 has measured your magical aptitude__')
	# TODO upload image with text

async def status_window(message):
	try:
		user_data = [Points.current(message.from_user.id, 'HP'), Points.current(message.from_user.id, 'Coins'), Points.current(message.from_user.id, 'Mana') ]# get all of user's data in DB | False if user not in DB
		healthbar = Points.HealthBar(user_data[0]//10) # get the tens position in HP
		playerRank = RankingSystem(user_data[2])
		# playerRank = playerRank.getRank()
		user_data.append(playerRank.getRank())
		# if user_data: 
		# 	msg_content = f"**HP:** {user_data[0]}/100\n[ {healthbar} ]\n**Coins:** 💰{user_data[1]}\n**Mana:** {user_data[2]}\n**Rank:** {user_data[3]}"
	except: # if user not in DB
		msg_content = " Ă̴̗N̷̤͊ ̴̤̔E̶̝̊R̴̛͇R̸̗̐O̵̱̾R̸̦̀ ̶̬̃O̸̝͆C̴̛̠C̷̬͠Ȗ̷̟R̸͔̆E̸͔͛D̷͎͗ "
	# text = msg_formatter(msg_content, 'STATUS', message.from_user.mention) # format the text into RPG style
	return user_data

async def status_image(user_data, username):
	username_len = font.getlength(username)+10

	base_img = Image.open(f'{os.getcwd()}/todoer/utils/resources/status_base.png')
	drawInst = ImageDraw.Draw(base_img)

	x_axis = 580 - username_len/2
	drawInst.text((x_axis,320), username, font=font, fill=(255, 255, 255, 255))

	await hp_bar(user_data[0]//10, base_img.size)
	await rank_text(user_data[3], base_img)
	await Draw_coin_mana(str(user_data[2]), str(user_data[1]), base_img)
	hp_bar_img = Image.open(f'{os.getcwd()}/todoer/utils/resources/hp_bar.png')
	base_img.paste(hp_bar_img, mask=hp_bar_img)
	base_img.save(f'{os.getcwd()}/todoer/utils/resources/new_status.png') 

async def hp_bar(hp, size):
	bar = Image.new("RGBA", size, 0)
	bar_draw = ImageDraw.Draw(bar)

	top_left = [341,538]
	btm_right = [383,580]
	gap = 9
	for i in range(hp):
		bar_draw.rectangle([tuple(top_left), tuple(btm_right)], fill='white')
		top_left[0] = top_left[0]+gap+42
		btm_right[0] = btm_right[0]+gap+42
	
	bar.save(f'{os.getcwd()}/todoer/utils/resources/hp_bar.png') 

async def rank_text(Rank_ls, base_img):
	rank_name = Rank_ls[0]
	rank_name_len = (font.getlength(rank_name)+10)/2
	rank_symbol = Rank_ls[1]

	draw_rank = ImageDraw.Draw(base_img)
	draw_rank.text((640, 878), rank_symbol, fill='white', font=hebrew_font)
	draw_rank.text((780-rank_name_len, 900), rank_name, fill='white', font=font)

async def Draw_coin_mana(coins, mana, base):
	draw_text = ImageDraw.Draw(base)
	
	coins_len = (font.getlength(coins)+10)/2
	mana_len = (font.getlength(mana)+10)/2
	draw_text.text((780-coins_len, 650), coins, fill='white', font=font)
	draw_text.text((780-mana_len, 775), mana, fill='white', font=font)

