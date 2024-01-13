# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
# the Strings used for this "thing"
from translation import Translation
from utils import verify_user, check_token
from pyrogram import filters
from database.adduser import AddUser
from plugins.forcesub import handle_force_sub
from pyrogram import Client as Tech_VJ
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Tech_VJ.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.TECH_VJ_HELP_TEXT,
        reply_markup=Translation.TECH_VJ_HELP_BUTTONS,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Tech_VJ.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    if Config.TECH_VJ_UPDATES_CHANNEL is not None:
        back = await handle_force_sub(bot, update)
        if back == 400:
            return
    if len(update.command) != 2:
      
    # logger.info(update)
        await AddUser(bot, update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.TECH_VJ_START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.TECH_VJ_START_BUTTONS,
            reply_to_message_id=update.message_id
        )
        return
    data = update.command[1]

    if data.split("-", 1)[0] == "verify":
        userid = data.split("-", 2)[1]
        token = data.split("-", 3)[2]
        if str(update.from_user.id) != str(userid):
            return await update.reply_text(
                text="<b>ᴇxᴘɪʀᴇᴅ ʟɪɴᴋ ᴏʀ ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ !</b>",
                protect_content=True
            )
        is_valid = await check_token(bot, userid, token)
        if is_valid == True:
            await update.reply_text(
                text=f"<b>ʜᴇʟʟᴏ {update.from_user.mention} 👋,\nʏᴏᴜ ᴀʀᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ᴠᴇʀɪғɪᴇᴅ !\n\nɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ғᴏʀ ᴀʟʟ ᴜʀʟ ᴜᴘʟᴏᴀᴅɪɴɢ ᴛɪʟʟ ᴛᴏᴅᴀʏ ᴍɪᴅɴɪɢʜᴛ.</b>",
                protect_content=True
            )
            await verify_user(bot, userid, token)
        else:
            return await update.reply_text(
                text="<b>ᴇxᴘɪʀᴇᴅ ʟɪɴᴋ ᴏʀ ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ !</b>",
                protect_content=True
            )
