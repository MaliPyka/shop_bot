from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.Inline_Keyboards import admin_main_keyboard
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from database.requests import add_category, get_categories_name

admin_router = Router()

class Add(StatesGroup):
    waiting_category = State()
    waiting_name = State()
    waiting_description = State()
    waiting_quantity = State()
    waiting_price = State()

@admin_router.message(Command("admin"))
async def admin_cmd(message: Message, is_admin: bool):
    if not is_admin:
        await message.answer("Вы не являетесь админом!")
        return

    await message.answer("""⚙️ ПАНЕЛЬ УПРАВЛЕНИЯ KOTBASS ————————————————— 🛠 Статус системы: Online 👤 Доступ: Администратор

Используйте меню ниже для настройки склада, управления категориями и запуска рассылок. ————————————————— 👇 Выберите раздел:""", reply_markup=admin_main_keyboard())


@admin_router.callback_query(F.data == "add_product")
async def callback(callback: CallbackQuery):
    pass

@admin_router.callback_query(F.data == "add_category")
async def callback(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text("Введите название новой категории:")
    await state.set_state(Add.waiting_name)

@admin_router.message(Add.waiting_name)
async def waiting_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    name = data.get("name")
    all_categories = await get_categories_name()
    if name in all_categories:
        await message.answer(f"Категория {name} уже существует!")
        await state.clear()
        return
    await add_category(name)
    await state.clear()
    await message.answer(f"Категория {name} успешно добавлена!")

@admin_router.callback_query(F.data("delete_product_list"))
async def callback(query: CallbackQuery):
    pass

@admin_router.callback_query(F.data("delete_category_list"))
async def callback(query: CallbackQuery):
    pass

@admin_router.callback_query(F.data("admin_broadcast"))
async def callback(query: CallbackQuery):
    pass

@admin_router.callback_query(F.data("admin_stats"))
async def callback(query: CallbackQuery):
    pass