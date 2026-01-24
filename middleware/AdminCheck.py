from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from typing import Callable, Dict, Any, Awaitable

from database.requests import get_admins



class AdminCheck(BaseMiddleware):
    async def __call__(self, handler: Callable, event: TelegramObject, data: Dict[str, Any]) -> Any:

        user = data.get("event_from_user")
        if user:
            admins = await get_admins()
            data['is_admin'] = user.id in admins
        else:
            data['is_admin'] = False

        return await handler(event, data)