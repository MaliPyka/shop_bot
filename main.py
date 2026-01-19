import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from database.engine import engine, Base
import database.models

from database.engine import DB_URL
print("DB_URL =", DB_URL)

from handlers.user import router

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()
dp.include_router(router)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await create_db()
        print("УРА! Таблицы успешно созданы в базе данных.")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
