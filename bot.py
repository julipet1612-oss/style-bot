import os
from aiogram import Bot, Dispatcher, F
# ... остальные импорты

BOT_TOKEN = os.getenv("BOT_TOKEN")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

if not BOT_TOKEN or not REPLICATE_API_TOKEN:
    raise ValueError("Токены не найдены в переменных окружения")

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

bot = Bot(token=BOT_TOKEN)


