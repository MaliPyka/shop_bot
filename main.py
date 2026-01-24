import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from middleware.AdminCheck import AdminCheck

from database.engine import engine, Base

from database.engine import DB_URL
print("DB_URL =", DB_URL)

from handlers.user import router
from handlers.admin_panel import admin_router

load_dotenv()


bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

dp.message.middleware(AdminCheck())
dp.callback_query.middleware(AdminCheck())

dp.include_router(admin_router)
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
