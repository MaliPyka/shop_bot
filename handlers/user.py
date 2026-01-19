from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from database.requests import set_user

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await set_user(message.from_user.id,
                   message.from_user.username,
                   message.from_user.first_name)

    await message.answer(f"Привет, {message.from_user.username}!")



