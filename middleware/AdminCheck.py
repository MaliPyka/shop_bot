from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from typing import Callable, Dict, Any, Awaitable

from database.requests import get_admins



class AdminCheck(BaseMiddleware):
    async def __call__(self, handler: Callable, event: Message, data: Dict[str, Any]) -> Any:

        admins = await get_admins()
        user_id = event.from_user.id

        data['is_admin'] = user_id in admins

        return await handler(event, data)