"""

MIT License

Copyright (c) 2022 DɪʟᴜᴍBBᴀɴᴅᴀʀᴀ (github.com/DilumBBandara)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


"""

import requests
from requests import post,get
import pyrogram
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions
from pyrogram.types import (Message, InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent,
                            InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
from config import (bot_username, Discussion, CHANNEL, start_sticker_id, TG_API_HASH, TG_API_ID,
		    TG_BOT_TOKEN, C_CHANNEL, SUPPORT, OWNER , CO_OWNER)
from addusers import AddUserToDatabase, AddChatToDatabase
from Bot.inline import (help_msg, START_MESSAGE, START_MESSAGE_BUTTONS, WELLCOME_BUTTONS, HELP_MESSAGE_BUTTONS, VISIT_PM,
			BACK_BUTTONS, HELBACK_BUTTONS, logo)

bot = Client(
	"""telegram_bot""",
	api_id = f"{TG_API_ID}",
	api_hash = f"{TG_API_HASH}",
	bot_token = f"{TG_BOT_TOKEN}",
	)


@bot.on_message(filters.command("help") & filters.private)
def command2(bot, message):
	bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
	typingmsg=message.reply_text("🪄 Starting API..")
	typingmsg.edit("🗂️ Getting Your Information...")
	typingmsg.edit("🌪️ Testing Speed..)
	typingmsg.edit("📡 Connected On Emo Network..")
	text="""😇 Hello...\n \n🌺🍃 I'm a Powerfull Bot With Cool Modules. Add me to your groups! ♥️ & Enjoy! \n\n ✨️ For All Users \n\n 😇 Friendly Bot \n ⚡️ Fast Response \n 📡 24 Hours Active \n 🎃 New Theme \n 🧩 New API \n\n @ImRishmika | @EmoBotDevolopers 🇱🇰"""
	reply_markup=InlineKeyboardMarkup(HELP_MESSAGE_BUTTONS)
	message.reply(
                text=text,
                reply_markup=reply_markup,
                disable_web_page_preview=True,
                )

@bot.on_message(filters.command("help") & filters.group)
async def grouphelpmsg(bot, message):
	await AddChatToDatabase(bot, message)
	text="""» ʜᴇʟᴘ    """
	reply_markup = InlineKeyboardMarkup(VISIT_PM)
	message.reply(
		text=text,
		reply_markup=reply_markup,
		disable_web_page_preview=True,
		)

@bot.on_message(filters.command('start') & filters.group)
async def groupstartmsg(bot, message):
	await AddChatToDatabase(bot, message)
	text="""|     """
	reply_markup = InlineKeyboardMarkup(VISIT_PM)
	message.reply(
		text=text,
		reply_markup=reply_markup,
		disable_web_page_preview=True,
		)

@bot.on_message(filters.command('test') & filters.group)
def grouptestmsg(bot, message):
	text="""|     """
	reply_markup = InlineKeyboardMarkup(VISIT_PM)
	message.reply(
		text=text,
		reply_markup=reply_markup,
		disable_web_page_preview=True,
		)

@bot.on_message(filters.command("otpbomber") & filters.group)
def groupotpbombermsg(bot, message):
	text="""|    """
	reply_markup = InlineKeyboardMarkup(VISIT_PM)
	message.reply(
		text=text,
		reply_markup=reply_markup,
		disable_web_page_preview=True,
		)

@bot.on_message(filters.command('start') & filters.private)
async def command1(bot, message):
	#message.reply_photo(photo=f"{start_img}")
	await AddUserToDatabase(bot, message)
	await bot.send_sticker(message.from_user.id, start_sticker_id)
	await message.reply_text(text = START_MESSAGE,
		reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS),
		disable_web_page_preview=True,
		)

@bot.on_message(filters.command('test') & filters.private)
async def comantest(bot, message):
	await bot.send_chat_action(message.chat.id, enums.ChatAction.CHOOSE_STICKER)
	await bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEOr3RjWVfeQUqOb78J0biqcjSPGIleIgACYAAD29t-AAGGKUzOUOHn4SoE")


@bot.on_message(filters.command("otpbomber") & filters.private)
async def boomer(_, message):
	if len(message.command) < 2:
		return await message.reply_text("🧩 | Provide with a phone number. 😴")
	m = await message.reply_text(" 🌚 Booming...‼️ \n━━━━━API Running━━━━━")
	query = message.text.split(None, 1)[1] if len(message.command) < 3 else message.text.split(None, 1)[1].replace(" ", "%20")
	count=int(25)
	for i in range (0,count):
		z= "#..... "
		zzx=await message.reply_text("Successful... ⚠️️")
		r= "#..... "
		zzz=await message.reply_text("Successful... ⚠️️")
		g= "#..... "
		zzzz=await message.reply_text("Successful... ⚠️️")
		dil = await message.reply_text("   Done ‼️ \n━━━━━━━━━━━━━━")

@bot.on_callback_query()
def callback_query(Client, Callback_Query):
	if Callback_Query.data == "helpmenu":
		Callback_Query.edit_message_text(
			help_msg,
			reply_markup=InlineKeyboardMarkup(BACK_BUTTONS),
		)
	elif Callback_Query.data == "helback":
		Callback_Query.edit_message_text(
			START_MESSAGE,
			reply_markup=InlineKeyboardMarkup(HELP_MESSAGE_BUTTONS),
			disable_web_page_preview=True,
		)
	elif Callback_Query.data == "Back":
		Callback_Query.edit_message_text(
			START_MESSAGE,
			reply_markup=InlineKeyboardMarkup(START_MESSAGE_BUTTONS),
			disable_web_page_preview=True,
		)
	elif Callback_Query.data == "helhelpmenu":
		Callback_Query.edit_message_text(
			help_msg,
			reply_markup=InlineKeyboardMarkup(HELBACK_BUTTONS),
		)


from database import (
    get_served_users,
    add_served_user,
    remove_served_user,
    get_served_chats,
    add_served_chat,
    remove_served_chat
)


@bot.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(_, message):
    m = await message.reply_text(text=f"Getting Stats...")
    served_chats = len(await get_served_chats())
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    served_users = len(await get_served_users())
    served_users = []
    users = await get_served_users()
    for user in users:
        served_users.append(int(user["bot_users"]))

    await m.edit(
        text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{len(served_users)}`
👥 Groups : `{len(served_chats)}`
🚧 Total users & groups : {int((len(served_chats) + len(served_users)))} """)

async def broadcast_messages(user_id, message):
    try:
        await message.forward(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await remove_served_user(user_id)
        return False, "Deleted"
    except UserIsBlocked:
        await remove_served_user(user_id)
        return False, "Blocked"
    except PeerIdInvalid:
        await remove_served_user(user_id)
        return False, "Error"
    except Exception as e:
        return False, "Error"

@bot.on_message(filters.private & filters.command("bcast") & filters.user(OWNER) & filters.reply)
async def broadcast_message(_, message):
    b_msg = message.reply_to_message
    chats = await get_served_users()
    m = await message.reply_text("🔥 Broadcasting...")
    for chat in chats:
        try:
            await broadcast_messages(int(chat['bot_users']), b_msg)
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await m.edit(f"""
❤️‍🔥 | Broadcast Completed. ☘️""")


def start_bot():
	print ()
	print (logo)
	print (' [+] running...')
	bot.run()
	print (' [+] stopped !!')
	print ()


if __name__ == '__main__':
	start_bot()

