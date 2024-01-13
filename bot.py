import os
import logging
from config import Config
from pyrogram import Client as Tech_VJ
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    VJ = Tech_VJ("@BOT_X_BOT",
    bot_token=Config.TECH_VJ_BOT_TOKEN,
    api_id=Config.TECH_VJ_API_ID,
    api_hash=Config.TECH_VJ_API_HASH,
    plugins=plugins)
    VJ.run()
