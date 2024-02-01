from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from tgbot.keyboards.inline import get_back_keyboard, start_user_keyboard
from tgbot.misc.constants import START_TEXT

video_router = Router()


@video_router.callback_query(F.data == "continue_in_bot")
async def get_video_link(query: CallbackQuery):
    await query.message.delete()
    await query.message.answer(
        text="Enter the link or video_id to the video:",
        reply_markup=get_back_keyboard(),
    )


@video_router.callback_query(F.data == "get_back")
async def get_back(query: CallbackQuery):
    await query.message.edit_text(
        text=START_TEXT,
        reply_markup=start_user_keyboard(),
        disable_web_page_preview=True,
    )
