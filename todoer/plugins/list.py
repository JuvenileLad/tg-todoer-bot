from ..utils.db_handler import get_tasksList
from ..client import app
import asyncio, re
from pyrogram import filters

@app.on_message(filters.command("list"))
async def lsTasks(_, message):
	await message.delete()
	await list_tasks(message.chat.id, message.from_user.id)
	
async def list_tasks(chat_id, user_id):
	list = get_tasksList(user_id) # task message_id(s) in a list
	if list:
		task_msgObjects = await app.get_messages(chat_id, list, replies=0) # fetch content of the message
		all_text = ''''''
		for i in task_msgObjects:
			task_name = re.findall('\n\n([^╘]*)\n\n', i.text)[0] # task ID comes after ╘ symbol
			all_text = all_text+(f"[#{task_name[0]}{i.id}] {task_name}\n")
		all_text += '\n__Click on the # hashtag to search for the message\n__'
		text = [all_text[i:i+4096] for i in range(0, len(all_text), 4096)] # telegram text size limit is 4096
		for i in text:
			li = await app.send_message(chat_id, i)
	else:
		text = 'No tasks found'
		li = await app.send_message(chat_id, text)
	
	await asyncio.sleep(20)
	await li.delete() # delete after 20 seconds