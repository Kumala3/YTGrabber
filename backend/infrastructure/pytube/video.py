from ast import List
from pytube import YouTube
from pytube.exceptions import (
    PytubeError,
    MaxRetriesExceeded,
    RegexMatchError,
    HTMLParseError,
    VideoUnavailable,
)


class Video:
    def get_video_info(self, video_url: str):
        try:
            yt = YouTube(video_url)
            channel_url = yt.channel_url
            author = yt.author
            title = yt.title
            length = yt.length
            views = yt.views
            publish_date = yt.publish_date.strftime("%Y-%m-%D")
            image_preview = yt.thumbnail_url
            data = {
                "channel_url": channel_url,
                "author": author,
                "title": title,
                "length": length,
                "views": views,
                "publish_date": publish_date,
                "image_preview": image_preview,
            }
            return data
        
        except RegexMatchError:
            return "Make sure URL is correct.Regex pattern did not return any matches."
        except MaxRetriesExceeded:
            return "Make sure URL is correct. Maximum number of retries exceeded"
        except HTMLParseError:
            return "Make sure URL is correct. HTML could not be parsed/processed"
        except PytubeError:
            return "Base pytube exception that all others inherit. Make sure URL is correct"

    def get_video_details(self, video_url: str):
        try:
            streams = (
                YouTube(video_url)
                .streams.filter(adaptive=True, file_extension="mp4", type="video")
                .order_by("resolution")
                .desc()
            )

            result = [(stream.resolution, round(stream.filesize_mb, 1)) for stream in streams]
            return result
        except VideoUnavailable as exception:
            if exception.__class__.__name__ == "AgeRestrictedError":
                return "Video is age restricted, and cannot be accessed without OAuth."
            if exception.__class__.__name__ == "LiveStreamError":
                return "Video is streaming live and cannot be loaded"
            if exception.__class__.__name__ == "VideoPrivate":
                return "Video is a private video"
            if exception.__class__.__name__ == "RecordingUnavailable":
                return "Video does not have a live stream recording available"
            if exception.__class__.__name__ == "MembersOnly":
                return "Video is for members only"
            if exception.__class__.__name__ == "VideoRegionBlocked":
                return "Video is not available in your region"
