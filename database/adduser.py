# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client
from database.access import techvj
from pyrogram.types import Message
from config import Config

LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""


async def AddUser(bot: Client, update: Message):
    if not await techvj.is_user_exist(update.from_user.id):
           await techvj.add_user(update.from_user.id)
           await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, LOG_TEXT_P.format(update.from_user.id, update.from_user.mention))
