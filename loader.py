import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv.main import load_dotenv
import os

load_dotenv()


# bot token from env
BOT_TOKEN=os.environ.get('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)
# PROXY_URL = "http://proxy.server:3128"



# init main bot
bot = Bot(token=BOT_TOKEN, parse_mode="markdown") #, proxy=PROXY_URL)
dp = Dispatcher(bot)