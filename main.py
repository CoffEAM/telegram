from handlers.time_table import router as time_tables
from aiogram import Bot,Dispatcher, types
import asyncio
from config import config_sets
import logging
bot = Bot(token=config_sets.token.get_secret_value())
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


async def main():
    dp.include_routers(time_tables)
    await dp.start_polling(bot)
asyncio.run(main())
