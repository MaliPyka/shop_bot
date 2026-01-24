from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.Inline_Keyboards import admin_main_keyboard, button_back
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from database.requests import add_category, get_categories_name, get_categories

admin_router = Router()

class Add(StatesGroup):
    waiting_category = State()
    waiting_name = State()
    waiting_description = State()
    waiting_quantity = State()
    waiting_price = State()
    waiting_name_item = State()

@admin_router.message(Command("admin"))
@admin_router.callback_query(F.data == "back")
async def admin_cmd(event: Message | CallbackQuery, is_admin: bool):
    if not is_admin:
        target = event if isinstance(event, Message) else event.message
        await target.answer("Вы не являетесь админом!")
        return

    text = (
        "⚙️ ПАНЕЛЬ УПРАВЛЕНИЯ KOTBASS\n"
        "—————————————————\n"
        "🛠 Статус системы: Online\n"
        "👤 Доступ: Администратор\n\n"
        "Используйте меню ниже для настройки склада...\n"
        "—————————————————\n"
        "👇 Выберите раздел:"
    )
    kb = admin_main_keyboard()

    if isinstance(event, Message):
        await event.answer(text, reply_markup=kb)
    elif isinstance(event, CallbackQuery):
        await event.message.edit_text(text, reply_markup=kb)
        await event.answer()


@admin_router.callback_query(F.data == "add_product")
async def callback(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    categories = await get_categories()
    list_categories = "\n".join([f"{c.id}. {c.name}" for c in categories])
    await callback.message.edit_text(f"Выберите категорию(номер) товара:\n{list_categories} ")
    await state.set_state(Add.waiting_category)


@admin_router.message(Add.waiting_category)
async def choose_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.edit_text("Введите название товара:")
    await state.set_state(Add.waiting_name_item)


@admin_router.message(Add.waiting_name_item)
async def save_item_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)


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
    await message.answer(f"Категория {name} успешно добавлена!", reply_markup=button_back())

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