from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode

from tgbot.keyboards.inline import start_user_keyboard
from tgbot.misc.constants import START_TEXT
from config import Config

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, config: Config):
    await message.reply(
        text=START_TEXT,
        reply_markup=start_user_keyboard(config.misc.web_app_url),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
