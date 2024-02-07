from pytube import YouTube
from pytube.exceptions import PytubeError


class Video:
    def __init__(self, video_url: str):
        self.video_url = video_url
        
    def get_video_info(self):
        try:
            author = YouTube(self.video_url).author
            title = YouTube(self.video_url).title
            length = YouTube(self.video_url).length
            views = YouTube(self.video_url).views
            publish_date = YouTube(self.video_url).publish_date
            image_preview = YouTube(self.video_url).thumbnail_url
            data =  {   
                "author": author,
                "title": title,
                "length": length,
                "views": views,
                "publish_date": publish_date,
                "image_preview": image_preview
            }
            return data
        except PytubeError as e:  # Broadening the catch here for debugging
            return str(e)
