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


def confirm_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="✅ Confirm", callback_data="confirm")
    keyboard.button(text="❌ Cancel", callback_data="cancel")

    return keyboard.as_markup()


def resolutions_keyboard(video_data: list) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    for item in video_data:
        keyboard.button(
            text=f"✴{item[0]} ➡ {item[1]}mb", callback_data=f"res_{item[0]}"
        )

    keyboard.button(text="⬅️ Back", callback_data="get_back_menu")
    keyboard.adjust(1,1)        

    return keyboard.as_markup()

