import os
import pyrogram
from config import bot_username, Discussion, CHANNEL, C_CHANNEL, SUPPORT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

help_msg = '✘ Help Menu ✘ \n \n 💠 | All Commands 🌺 \n \n » /start \n » /help\n » /bomb \n » /test\n  » /song'


START_MESSAGE = "😇 Hello...\n \n🌺🍃 I'm a Assistant Bot Of Rishmika Sandanu. Add me to your groups! ♥️ & Enjoy! \n\n ✨️ For All Users \n\n 😇 Friendly Bot \n ⚡️ Fast Response \n 📡 24 Hours Active \n 🎃 New Theme \n 🧩 New API \n\n @ImRishmika | @EmoBotDevolopers 🇱🇰"


START_MESSAGE_BUTTONS = [
	[
	InlineKeyboardButton('📡 Bot Status 📡', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('</> ємσ вσт ∂єνσℓσρєʀѕ 🇱🇰', url=f't.me/EmoBotDevolopers'),
	InlineKeyboardButton('🍁 Support 🍁', url=f'https://t.me/EmoBotSupport'),
	],
	[
	InlineKeyboardButton('Devoloper 🧑‍💻', url=f'https://t.me/ImRishmika')
	
	],
	[
	InlineKeyboardButton(text='🎯 Help And Commands 🎯', callback_data='helpmenu'),
	],
	[
	InlineKeyboardButton(text='➕ Add Me to Your Group ➕', url=f'http://t.me/{bot_username}?startgroup=true'),
	],
]

WELLCOME_BUTTONS = [
	[
	InlineKeyboardButton('✘ Emo Bot Devoopers ✘', url=f'https://t.me/EmoBotDevolopers'),
	],
]

HELP_MESSAGE_BUTTONS = [
	[
	InlineKeyboardButton('📡Bot Status 📡', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('🌐 All Commands 🌐', callback_data='helhelpmenu'),
	],
	[
	InlineKeyboardButton('⚙ Restart ⚙', url=f'https://t.me/{bot_username}?start'),
	],
	[
	InlineKeyboardButton(text='🔥━━━━━EmoDevolopers━━━━━🔥', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton(text='➕ Add Me to Your Group ➕', url=f'http://t.me/{bot_username}?startgroup=true'),
	],
]


VISIT_PM = [
	[
	InlineKeyboardButton('📡 Bot Status 📡', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('🪩 Visit PM 🪩', url=f'https://t.me/{bot_username}?start'),
	]
	
	
        
	
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

