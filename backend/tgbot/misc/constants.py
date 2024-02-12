from aiogram.utils.markdown import hlink
from datetime import timedelta


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
    time_delta = timedelta(seconds=data['length'])
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
 
    text = f"""
<b>This is the video are you looking for?</b>

Channel: {hlink(data['channel_url'], url=data['channel_url'])}
Author: <b>{data['author']}</b>
Title: <b>{data['title']}</b>
Length: {hours:02}:{minutes:02}:{seconds:02}
Views: {data['views']}
Publish Date: {data['publish_date']}
"""
    return text

