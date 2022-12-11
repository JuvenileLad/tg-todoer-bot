from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from ..client import app
from .db_handler import Task
from .format_text import msg_formatter 

async def newTask(message):
	text = msg_formatter(f"`{message.text}`", 'PENDING', f'#{message.text[0]}{message.id+1}')
	task_id = message.id + 1
	user_id = message.from_user.id
	task = Task(user_id, task_id)
	task.add_task()
	btn = [
	[InlineKeyboardButton(f"✅ Done", callback_data=f"done_{task_id}"), InlineKeyboardButton(f"❎ Missed", callback_data=f"missed_{task_id}")],
	[InlineKeyboardButton(f"😣 Postpone", callback_data=f"postponed_{task_id}")]
	]
	await app.send_message(message.chat.id, text, reply_markup=InlineKeyboardMarkup(btn))

async def remove_task(cb, cb_type):
	task_id = cb.data.split("_")[1]
	user_id = cb.from_user.id
	task = Task(user_id, task_id)
	
	text = task.remove_task(cb_type)
	return text



