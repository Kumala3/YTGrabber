from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from tgbot.keyboards.inline import start_keyboard, back_keyboard, menu_keyboard
from tgbot.misc.constants import start_text
from tgbot.misc.states import VideoUrl
from config import Config

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, config: Config):
    await message.reply(
        text=start_text(config.misc.repo_url),
        reply_markup=start_keyboard(config.misc.web_app_url),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


@user_router.callback_query(F.data == "continue_in_bot")
async def menu(query: CallbackQuery):
    await query.message.edit_text(
        text="Menu",
        reply_markup=menu_keyboard(),
    )


@user_router.callback_query(F.data == "profile")
async def get_profile(query: CallbackQuery):
    await query.message.edit_text(
        text="Profile",
        reply_markup=back_keyboard("menu"),
    )


@user_router.callback_query(F.data == "download_video")
async def get_video_link(query: CallbackQuery, state: FSMContext):
    await query.message.edit_text(
        text="Enter the link or video_id to the video:",
        reply_markup=back_keyboard("menu"),
    )
    await state.set_state(VideoUrl.video_url)


@user_router.message()
async def undefined_message(message: Message):
    await message.answer(
        "I don't understand you, please use the menu to navigate.\nUse /start to open main menu"
    )


@user_router.callback_query(F.data == "downloaded_videos")
async def get_downloaded_videos(query: CallbackQuery):
    await query.message.edit_text(
        text="Here are your downloaded videos:",
        reply_markup=back_keyboard("menu"),
    )


@user_router.callback_query(F.data == "support")
async def get_support(query: CallbackQuery):
    await query.message.edit_text(
        text="Contact support:",
        reply_markup=back_keyboard("menu"),
    )


@user_router.callback_query(F.data == "get_back_start")
async def get_back(query: CallbackQuery, config: Config):
    await query.message.edit_text(
        text=start_text(config.misc.repo_url),
        reply_markup=start_keyboard(config.misc.web_app_url),
        disable_web_page_preview=True,
    )


@user_router.callback_query(F.data == "get_back_menu")
async def back_to_menu(query: CallbackQuery):
    await query.message.edit_text(
        text="Menu",
        reply_markup=menu_keyboard(),
    )
