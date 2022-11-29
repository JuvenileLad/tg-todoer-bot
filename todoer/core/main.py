from pyrogram import filters
from pyrogram.types.bots_and_keyboards import callback_query
import re
from ..client import app
from ..utils.task_handler import newTask, remove_task, msg_formatter
from ..plugins.status import status_window
from ..plugins.list import list_tasks
from ..plugins.leaderboard import _leaderboard
from ..plugins.start_menu import startm
from ..plugins.help_menu import helpm
from ..plugins.shop_front import shop

@app.on_message(filters.command("help"))
async def start(_, message):
	await message.reply_text("help is here!")

@app.on_message(filters.text)
async def task(_, message):
	msg = message
	if msg.entities == None:
		await newTask(message)
		await message.delete()

@app.on_callback_query()
async def task_btn(app, cb :callback_query):
	# text = ["Task Done", "Task Missed", "Task Postponed"]
	cb_type = cb.data.split("_")[0]
	alert_text = await remove_task(cb, cb_type)

	task = re.findall('\n\n([^╘]*)\n\n', cb.message.text)[0]

	text = msg_formatter(f"`{task}`", cb_type.upper(), f"#{task[0]}{cb.message.id+1}")
	await cb.answer(text=alert_text)
	await cb.message.edit_text(text)