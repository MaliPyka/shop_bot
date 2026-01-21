from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def get_start_keyboard() -> InlineKeyboardMarkup:

    button_info = InlineKeyboardButton(text="Информация",
                                       callback_data="info")

    button_profile = InlineKeyboardButton(text="Профиль",
                                          callback_data="profile")

    return InlineKeyboardMarkup(inline_keyboard=[[button_info], [button_profile]])

