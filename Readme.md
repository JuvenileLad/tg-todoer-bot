# Telegram Todoer Bot
## A telegram bot for keeping track of your daily tasks with a RPG-style twist.

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/JuvenileLad/tg-todoer-bot)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg?&style=flat-square)](https://github.com/JuvenileLad/tg-todoer-bot#copyright--license)

* *This bot is still in early development and needs a lot of work. Any and all suggestions are appreciated.*

```
➤ KANG AT YOUR OWN RISK: Your Telegram account may get banned in case of API abuse.
➤ I AM NOT RESPONSIBLE IF YOUR ACCOUNT GETS BANNED.
➤ I AM NOT RESPONSIBLE FOR ANY IMPROPER USE OF THIS BOT.
```

### <div id="gamemech">GAME MECHANICS</div>

- User adds a task by simply sending a text message to the bot (the text is the task itself), this makes them part of the game and they get 100% HP along with 0 Coins and 0 Mana.

- Various [task-actions](#task-actions) have varied effects on the Player's HP and Coins:

	- Completing a task (`Done`) will increase the Player's Coins by a random value between 1-5
	- Not completing a task (`Missed`) will decrease the Player's HP by a random value between 10-20
	- `Postponed` task will decrease the Player's Coins by a random value between 1-3

- Coins can be used to purchase Mana Potion from the shop. The Mana determines a Player's position in the leaderboard.

- If a Player's HP reaches 0, the Player's Coins and Mana are reset to 0 and HP is reset to 100%.

- the `/status` command can be used to generate a player report with all their relevant information including their [rank](#ranking-system).

- Many elements of the bot are inspired by the Japanese anime _Mairimashita! Iruma-kun_.
#### <div id='ranking-system'>Ranking System:</div>
The ranking system works separately from the leaderboard. The rank of the player is also based on their Mana. This system is based on the Gematria system.

<table>
<tr><th>Rank</th><th>Required Mana</th></tr>
<tr><td>Unranked</td><td>1</td></tr>
<tr><td>Aleph</td><td>90</td></tr>
<tr><td>Bet</td><td>178</td></tr>
<tr><td>Gimmel</td><td>266</td></tr>
<tr><td>Daleth</td><td>354</td></tr>
</table>

#### <div id='task-actions'>Task-Actions:</div>
- [✅](button_id_1): Marks the task as done.
- [❎](button_id_2): Marks the task as Missed.
- 😣: Marks the task as Postponed.

### Available Commands:
- `/start`: Start the bot.
- `/shop` : View the shop.
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

### <div id="config">Configuration</div>
copy the contents of `config.env_sample` to a new file `config.env` and then edit the following values:
*(all the values need to be inside double quotes)*

- in `SESSION_NAME` enter whatever you want as session name in telegram
- enter telegram API Hash in `API_HASH` & API ID in `API_ID`
- enter telegram bot token in `BOT_TOKEN`
- enter the MongoDB URL in `DATABASE_URL`.

Now run the bot by using the following command:
	`python3 -m todoer`

Or you can deploy on Heroku :

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/JuvenileLad/tg-todoer-bot)

> No need to fill config.env file when deploying on Heroku.
## Notes:
### Plugins System:
I've tried to add a plugins system in which new plugins can be directly added to `todoer/plugins` folder, and imported in `main.py`. Plugins like Item Shop, Pet Shop etc. can be added that way.
However, Plugin System requires a lot more testing.

### Logging:
There is next to no logging in the app (not even print statements). That is because I've never done logging before since all my programs used to be smaller in scale and print statements got the job done, but since this is a large scale program (with plugins and everything), I plan on implementing proper logging in the app as soon as possible.

### Design Pattern:
There is no design pattern and I'd really appreciate any advice regarding that. I understand that the structure of the program is not sustainable but I don't have any idea what to begin with.
