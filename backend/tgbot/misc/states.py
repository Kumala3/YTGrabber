from aiogram.fsm.state import StatesGroup, State


class VideoUrl(StatesGroup):
    video_url = State()
