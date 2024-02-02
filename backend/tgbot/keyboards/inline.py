from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo, InlineKeyboardMarkup


def start_keyboard(url: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="📱 Go to the application",
        web_app=WebAppInfo(url=url),
    )
    keyboard.button(text="Continue in the bot ➡️", callback_data="continue_in_bot")

    return keyboard.as_markup()


def back_keyboard(url: str = None) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="⬅️ Back", callback_data=f"get_back_{url}")

    return keyboard.as_markup()


def menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="👤 Profile", callback_data="profile")
    keyboard.button(text="📞 Support", callback_data="support")
    keyboard.button(text="📺 Download video", callback_data="download_video")
    keyboard.button(text="📫 Downloaded_videos", callback_data="downloaded_videos")
    keyboard.button(text="⬅️ Back", callback_data="get_back_start")

    keyboard.adjust(2, 2, 1)

    return keyboard.as_markup()
