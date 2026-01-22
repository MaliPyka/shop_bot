from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.Inline_Keyboards import admin_main_keyboard

admin_router = Router()



@admin_router.message(Command("admin"))
async def admin_cmd(message: Message, is_admin: bool):
    if not is_admin:
        await message.answer("Вы не являетесь админом!")
        return

    await message.answer("""⚙️ ПАНЕЛЬ УПРАВЛЕНИЯ KOTBASS ————————————————— 🛠 Статус системы: Online 👤 Доступ: Администратор

Используйте меню ниже для настройки склада, управления категориями и запуска рассылок. ————————————————— 👇 Выберите раздел:""", reply_markup=admin_main_keyboard())




