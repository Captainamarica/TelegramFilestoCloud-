#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


ENV = bool(os.environ.get('ENV', False))
try:
  if ENV:
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    APP_ID = os.environ.get('APP_ID')
    API_HASH = os.environ.get('API_HASH')
  else:
    from sample_config import config
    BOT_TOKEN = config.BOT_TOKEN
    APP_ID = config.APP_ID
    API_HASH = config.API_HASH
except KeyError:
  LOGGER.error('One or more configuration values are missing exiting now.')
  exit(1)


class msg():
    source = "\nsource:https://github.com/Abhijith-cloud/Telegram-MixDrop-Bot"
    start = "\n<b>This bot uploads telegram files to mixdrop.co @thankappan369</b>"
    error = "something is went wrong\n{error} \ncontact admin @thankappan369"
    help = "Usage: <b>Send any file or URL and the bot will upload it to mixdrop.co</b>"
