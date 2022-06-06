from pyrogram import filters
from ..client import app

@app.on_message(filters.command("help"))
async def helpm(_, message):
    text = "__Help Menu Coming Soon__"
    await app.send_message(message.chat.id, text)