from pyrogram import idle 
from todoer.client import app

app.start()
print("<Initialized>")
idle()
app.stop()
