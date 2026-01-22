from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from database.requests import set_user
from keyboards.Inline_Keyboards import get_start_keyboard

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await set_user(message.from_user.id,
                   message.from_user.username,
                   message.from_user.first_name)

    await message.answer("""Добро пожаловать в Kotbass Shop! 👋

Мы подготовили для тебя лучшие предложения по электронике в Тбилиси. 🇬🇪

🛒 Внутри каталога: • Новинки смартфонов и гаджетов • Аксессуары на любой вкус • Быстрая доставка прямо в руки

————————————————— 👇 Жми «Каталог», чтобы начать покупки:""",reply_markup=get_start_keyboard())







