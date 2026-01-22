from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def get_start_keyboard() -> InlineKeyboardMarkup:

    button_catalog = InlineKeyboardButton(text="🛒 Каталог",
                                       callback_data="catalog")

    button_basket = InlineKeyboardButton(text="🧺 Корзина",
                                          callback_data="basket")

    button_orders = InlineKeyboardButton(text="📦 Мои заказы",
                                         callback_data="orders")

    button_info = InlineKeyboardButton(text="ℹ️ О магазине/Доставка/Контакты",
                                       callback_data = "info")


    return InlineKeyboardMarkup(inline_keyboard=[[button_catalog], [button_basket], [button_orders], [button_info]])


def admin_main_keyboard():
    buttons = [
        # Первый ряд: Добавление
        [
            InlineKeyboardButton(text="➕ Товар", callback_data="add_product"),
            InlineKeyboardButton(text="➕ Категорию", callback_data="add_category")
        ],
        # Второй ряд: Удаление
        [
            InlineKeyboardButton(text="🗑 Удалить товар", callback_data="delete_product_list"),
            InlineKeyboardButton(text="🗑 Удалить категорию", callback_data="delete_category_list")
        ],
        # Третий ряд: Сервис
        [
            InlineKeyboardButton(text="📢 Рассылка", callback_data="admin_broadcast"),
            InlineKeyboardButton(text="📊 Статистика", callback_data="admin_stats")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

