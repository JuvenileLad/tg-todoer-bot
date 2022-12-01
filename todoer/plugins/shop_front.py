from ..client import app
from ..utils.shop_item import getShop, buy_item
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from ..utils.db_handler import Points, user_inDB
from pyrogram.types.bots_and_keyboards import callback_query
from pyrogram import filters
import re

@app.on_message(filters.command('shop'))
async def shop(_, message):
    if not user_inDB(message.chat.id):
        await message.reply_text("Shop is not available for users with no coins.")
        return
    Coins = Points.current(message.chat.id, 'Coins')
    shop_items = await getShop()
    btns = []
    text = f'**SHOP**\n[You have:💰 {Coins}]\n\n'
    for s in shop_items:
        text+=f'{s.name} (💰{s.price})\n__{s.description}__\n\n'
        btn = [InlineKeyboardButton(f"{s.name}", callback_data=f"buy_{s.name}_{s.price}_{s.effect}")]
        btns.append(btn)
    await app.send_message(message.chat.id,text,reply_markup = InlineKeyboardMarkup(btns))

@app.on_callback_query(filters.regex(r"buy_(.*)"))
async def buy_cb(app, cb:callback_query):
    data = cb.data.split("_")
    item_price = int(data[2])
    player_coins = Points.current(cb.from_user.id, 'Coins')

    if player_coins<item_price:
        await cb.answer("Insufficient Funds")
    else:
        alert = await buy_item(data, cb.from_user.id)
        await cb.answer(alert)

        original_text = cb.message.text
        original_coins = int(re.findall("(?<=\💰[ \t])(.*?)(?=\])", original_text)[0])
        original_coins = f"💰 {original_coins}"
        player_coins = str(Points.current(cb.from_user.id, 'Coins'))
        new_text = re.sub(original_coins, f"💰 {player_coins}", original_text)
        await app.edit_message_text(chat_id=cb.from_user.id, message_id=cb.message.id, text=new_text, reply_markup = cb.message.reply_markup)