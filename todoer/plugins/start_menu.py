from pyrogram import filters
from ..client import app

@app.on_message(filters.command("start"))
async def startm(_, message):
    text = "**Hi! I am todoer-bot.**\nI can keep track of all yours tasks at hand\nwith an RPG-style twist.\n\n__To add a new task, just send me name of the task__\n__(Bot is still in <u>beta version</u> so some bugs are expected__\n__Report any bugs to @juve_watson)__"
    await app.send_message(message.chat.id, text)