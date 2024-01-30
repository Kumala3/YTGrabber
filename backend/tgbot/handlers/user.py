from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.keyboards.miniapp import get_miniapp_link
from config import Config

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, config: Config):
    await message.reply(
        text="Greetings dear user!", reply_markup=get_miniapp_link(config.tg_bot.web_app_url)
    )
