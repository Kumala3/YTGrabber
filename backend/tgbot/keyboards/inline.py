from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo
from config import load_config


def get_back_keyboard():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Get back", callback_data="get_back")

    return keyboard.as_markup()


def start_user_keyboard():
    config = load_config(".env")
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="📱 Go to the application",
        web_app=WebAppInfo(url=config.misc.web_app_url),
    )
    keyboard.button(text="Continue in the bot ➡️", callback_data="continue_in_bot")

    return keyboard.as_markup()
