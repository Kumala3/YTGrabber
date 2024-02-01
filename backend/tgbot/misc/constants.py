from aiogram.utils.markdown import hlink
from config import load_config

config = load_config(".env")

WELCOME_TEXT = "<b>Welcome to the amazing bot that lets you download absolutely any YouTube video for free at all!</b>\n"

GITHUB_REPO_URL = hlink("GitHub", url=config.misc.github_repo_url)

DESCRIPTION_PROJECT_TEXT = f"""
This project is fully <b>open source</b> and available on GitHub, thus epitomizes the spirit of collaboration as well as innovation.\n
Downloading with <b>video ID</b> or even <b>direct URL</b> is just a click away.\n
Check out the {GITHUB_REPO_URL} repo for more details and dive into a world of limitless video downloading possibilities!
"""

START_TEXT = WELCOME_TEXT + DESCRIPTION_PROJECT_TEXT
