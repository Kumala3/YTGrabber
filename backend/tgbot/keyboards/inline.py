from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo


def get_back_keyboard():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Get back", callback_data="get_back")

    return keyboard.as_markup()


def start_user_keyboard(url: str):
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="📱 Go to the application",
        web_app=WebAppInfo(url=url),
    )
    keyboard.button(text="Continue in the bot ➡️", callback_data="continue_in_bot")

    return keyboard.as_markup()
