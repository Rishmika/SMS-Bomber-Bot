import os
import pyrogram
from config import bot_username, Discussion, CHANNEL, C_CHANNEL, SUPPORT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

help_msg = '✘ Help Menu ✘ \n \n 💠 | All Commands 🌺 \n \n    » /start \n    » /help\n    » /otpbomber\n    » /test'


START_MESSAGE = "💠 | Hello... 😴\n \n🌺🍃 I'm a Powerfull Bot With Cool Modules. Add me to your groups! ♥️ & Enjoy!!\n \n❤️‍🔥 Made by @Team_Mars_11 | @CGSUpdates 🇱🇰"


START_MESSAGE_BUTTONS = [
	[
	InlineKeyboardButton('☃︎━━━━━━━━━━━━━━☃︎', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('☘️ CHANNEL ☘️', url=f'https://t.me/{C_CHANNEL}'),
	InlineKeyboardButton('🍁 Support 🍁', url=f'https://t.me/{SUPPORT}'),
	],
	[
	InlineKeyboardButton('☘️ CHANNEL ☘️', url=f'https://t.me/{CHANNEL}'),
	InlineKeyboardButton('🍁 Discussion 🍁', url=f'https://t.me/{Discussion}'),
	],
	[
	InlineKeyboardButton(text='🌺 Help 🌺', callback_data='helpmenu'),
	],
	[
	InlineKeyboardButton(text='➕ Add Me to Your Group ➕', url=f'http://t.me/{bot_username}?startgroup=true'),
	],
]

WELLCOME_BUTTONS = [
	[
	InlineKeyboardButton('🌺 CHANNEL 🌺', url=f'https://t.me/{CHANNEL}'),
	],
]

HELP_MESSAGE_BUTTONS = [
	[
	InlineKeyboardButton('━━━━━━━━━━━━━━', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('🌐 All Commands 🌐', callback_data='helhelpmenu'),
	],
	[
	InlineKeyboardButton('⚙ Restart ⚙', url=f'https://t.me/{bot_username}?start'),
	],
	[
	InlineKeyboardButton(text='━━━━━━━━━━━━━━', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton(text='➕ Add Me to Your Group ➕', url=f'http://t.me/{bot_username}?startgroup=true'),
	],
]


VISIT_PM = [
	[
	InlineKeyboardButton('━━━━━━━━━━━━━━', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('☘️ Visit PM ☘️', url=f'https://t.me/{bot_username}?start'),
	],
	[
	InlineKeyboardButton('❤️‍🔥 CHANNEL ❤️‍🔥', url=f'https://t.me/{CHANNEL}'),
        InlineKeyboardButton('❤️‍🔥 CHANNEL ❤️‍🔥', url=f'https://t.me/{C_CHANNEL}'),
	],
]


BACK_BUTTONS = [
	[
	InlineKeyboardButton('🔙 Back', callback_data="Back"),
	],
]

HELBACK_BUTTONS = [
	[
	InlineKeyboardButton('🔙 Back', callback_data="helback"),
	],
]


logo="""

╭━━━┳━╮╭━┳━━━╮╱╱╭━━╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭━━╮╱╱╱╭╮
┃╭━╮┃┃╰╯┃┃╭━╮┃╱╱┃╭╮┃╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱┃╭╮┃╱╱╭╯╰╮
┃╰━━┫╭╮╭╮┃╰━━╮╱╱┃╰╯╰┳━━┳╮╭┫╰━┳━━┳━╮┃╰╯╰┳━┻╮╭╯
╰━━╮┃┃┃┃┃┣━━╮┣━━┫╭━╮┃╭╮┃╰╯┃╭╮┃┃━┫╭╯┃╭━╮┃╭╮┃┃
┃╰━╯┃┃┃┃┃┃╰━╯┣━━┫╰━╯┃╰╯┃┃┃┃╰╯┃┃━┫┃╱┃╰━╯┃╰╯┃╰╮
╰━━━┻╯╰╯╰┻━━━╯╱╱╰━━━┻━━┻┻┻┻━━┻━━┻╯╱╰━━━┻━━┻━╯

"""

