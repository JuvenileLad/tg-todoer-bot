from pyrogram import idle 
from todoer.client import app, version, session

app.start()
print(f"Initialised {session} v{version}")
idle()
app.stop()
