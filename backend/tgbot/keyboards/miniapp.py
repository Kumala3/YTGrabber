from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo

def get_miniapp_link(url: str):
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="📱 Go to the application",
        web_app=WebAppInfo(url=url)
    )
    
    return keyboard.as_markup() 
