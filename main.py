import os
import logging
from main_bot.start_handler import dp
from aiogram import Bot
import asyncio
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(TOKEN)
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
