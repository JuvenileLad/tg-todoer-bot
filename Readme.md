# Telegram Todoer Bot
## A telegram bot for saving your daily Tasks with an RPG-style twist.
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/JuvenileLad/Telegram-todoer-bot)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg?&style=flat-square)](https://github.com/JuvenileLad/Telegram-todoer-bot#copyright--license)
<h2 align="center"><b>Owner: <a href="https://telegram.dog/juve_watson">Juvenile Lad</a></b><br>
<b>Bot: <a href="https://telegram.dog/kalegobot">Kalego Sensei</a></b></h2>

```
➤ KANG AT YOUR OWN RISK: Your Telegram account may get banned in case of API abuse.
➤ I AM NOT RESPONSIBLE IF YOUR ACCOUNT GETS BANNED.
➤ I AM NOT RESPONSIBLE FOR ANY IMPROPER USE OF THIS BOT.
```

* *proper Readme soon.*
* *This bot is still in early development and needs a lot of work*

### Uses the following libraries:
- [Pyrogram (Telegram)](https://github.com/pyrogram/pyrogram)
- [Pymongo (MongoDB)](https://pymongo.readthedocs.io/en/stable/)

### Every User is a Player who has 100% HP and 0 Coins in the beginning of the game. Various `Task-Actions` have varied effects on the Player's HP and Coins.

- Completing a task (marking it as `Done`) will increase the Player's Coins by a random value between 1-5
- Not completing a task (marking as `Missed`) will decrease the Player's HP by a random value between 10-20
- `Postponing` a task will decrease the Player's Coins by a random value between 1-3
- **The Coins determine a Player's position in the leaderboard**.
- **If a Player's HP reaches 0, the Player's Coins are reset to 0 and HP is reset to 100%**.

#### any message sent to the bot is converted to a task with 3 accompanied buttons:
- [✅](button_id_1): Marks the task as done.
- [❎](button_id_2): Marks the task as Missed.
- 😣: Marks the task as Postponed.

### Available Commands:
- `/start`: Start the bot.
- `/help`: View help message.
- `/list`: Lists all the tasks.
- `/leaderboard`: Shows the leaderboard.
- `/status`: View status

## <div id="install">INSTALLATION</div>

### <div id="preq">Prequisites</div>
*Clone the repository*
```
git clone https://github.com/JuvenileLad/telegram-reddit-bot.git && cd telegram-reddit-bot
```
*Install the required python libraries*
```
pip3 install -U -r requirements.txt
```

*Obtain all the required API keys*

1) Telegram
	- Go to https://my.telegram.org/auth
	- Follow [this](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) guide to obtain Telegram *API hash* & *API key*
	- Obtain the *bot token* from https://t.me/BotFather
	<BR>
3) MongoDB
	- Follow [this guide](https://telegra.ph/How-to-get-MongoDB-URL-02-04)
	<br>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/JuvenileLad/tg-todoer-bot)

### <div id="config">Configuration</div>
copy the contents of `example_config.ini` to a new file `config.ini` and then edit the following values:
*(do not add quotes(" ") symbol in any value)*

- in `session_name` enter whatever you want as session name in telegram
- enter telegram API Hash in `api_hash` & API ID in `api_id`
- enter telegram bot token in `bot_token`
- enter the MongoDB URL in `url`.
- the `config.ini` file already consists of sample values, you just have to replace them

#### Now run the bot by using:
	python3 -m todoer

## Notes:
### Plugins System:
I've tried to add a plugins system in which new plugins can be directly added to `todoer/plugins` folder, and imported in `main.py`. 
Plugins like Item Shop, Pet Shop etc. can be added that way.

However, Plugins System requires a lot more testing.

### Logging:
There is next to no logging in the app (not even print statements). That is because I've never done logging before since all my programs used to be smaller in scale and print statements got the job done, but since this is a large scale program (with plugins and everything), I plan on implementing proper logging in the app as soon as possible.

