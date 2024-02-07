from aiogram.utils.markdown import hlink
from pytube.exceptions import RegexMatchError


def start_text(repo_url: str):
    welcome = "<b>Welcome to the amazing bot that lets you download absolutely any YouTube video for free at all!</b>\n"
    
    repo_url = hlink("GitHub", url=repo_url)

    description_project = f"""
This project is fully <b>open source</b> and available on GitHub, thus epitomizes the spirit of collaboration as well as innovation.\n
Downloading with <b>video ID</b> or even <b>direct URL</b> is just a click away.\n
Check out the {repo_url} repo for more details and dive into a world of limitless video downloading possibilities!
    """

    return welcome + description_project


def video_info_text(data: dict):
    try:
        text = f"""
This is the video are you looking for?:
Author: <b>{data['author']}</b>
Title: <b>{data['title']}</b>
Length: {data['length']}
Views: {data['views']}
Publish Date: {data['publish_date']}
"""
        return text
    except RegexMatchError:  # Broadening the catch here for debugging
        return "Regex Error you are trying to access a private video or another error occurred."
