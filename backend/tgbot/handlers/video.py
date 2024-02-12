from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from infrastructure.pytube.video import Video
from tgbot.misc.states import VideoUrl
from tgbot.keyboards.inline import back_keyboard, resolutions_keyboard, confirm_keyboard
from tgbot.misc.constants import video_info_text

video_router = Router()


@video_router.message(VideoUrl.video_url)
async def check_video(message: Message, state: FSMContext):
    video_url = message.text
    video_info = Video().get_video_info(video_url)

    if isinstance(video_info, dict):
        text = video_info_text(video_info)
        await message.answer(text=text, reply_markup=confirm_keyboard())
        await state.update_data(video_url=video_url)
    else:
        await message.answer(text=video_info, reply_markup=back_keyboard("menu"))


@video_router.callback_query(F.data == "cancel")
async def cancel_video(query: CallbackQuery):
    await query.message.edit_text(
        text="Enter the link or video_id to the video:",
        reply_markup=back_keyboard("menu"),
    )


@video_router.callback_query(VideoUrl.video_url, F.data == "confirm")
async def confirm_video(query: CallbackQuery, state: FSMContext):
    video = await state.get_data()
    video_details = Video().get_video_details(video.get("video_url"))

    try:
        if isinstance(video_details, list):
            await query.message.edit_text(
                text="Choose the resolution which you want to download!",
                reply_markup=resolutions_keyboard(video_details),
            )
            await state.clear()
        else:
            await query.message.edit_text(text=video_details, reply_markup=back_keyboard("menu"))
    except Exception as e:
        await query.message.edit_text(text=f"An error occurred: {str(e)}")

