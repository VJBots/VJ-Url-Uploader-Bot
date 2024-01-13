# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client as Tech_VJ
from pyrogram import filters
from config import Config
from database.access import techvj
from plugins.buttons import *

@Tech_VJ.on_message(filters.private & filters.command('total'))
async def sts(c, m):
    if m.from_user.id != Config.TECH_VJ_OWNER_ID:
        return 
    total_users = await techvj.total_users_count()
    await m.reply_text(text=f"Total user(s) {total_users}", quote=True)


@Tech_VJ.on_message(filters.private & filters.command("search"))
async def serc(bot, update):

      await bot.send_message(chat_id=update.chat.id, text="🔍 TORRENT SEARCH", 
      parse_mode="html", reply_markup=Button.BUTTONS01)
