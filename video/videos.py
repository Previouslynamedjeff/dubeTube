from comments.comments import Comment
videos = []

VIDEO_FOLDER = "/static/video/"

class Video:
    def __init__(self: object, video_id: str, thumbnail: str, extension: str, title: str, author: str, date: str, tags: list, transcript: str, summary: str):
        self.id = video_id
        self.thumbnail = f"{VIDEO_FOLDER}{thumbnail}"
        self.extension = extension
        self.title = title
        self.author = author
        self.date_posted = date 
        self.views = 0
        self.likes = 0
        self.dislikes = 0
        self.tags = tags
        self.comments = []
        self.transcript = transcript
        self.summary = summary
        
    def send_message(self, username, message):
        self.comments.append(Comment(username, message))

def add_video(video_id: str, thumbnail: str, extension: str, title: str, author: str, date: str, tags: list, transcript: str, summary: str):
    videos.append(Video(video_id, thumbnail, extension, title, author, date, tags, transcript, summary))

def find_by_id(v_id: str):
    for video in videos:
        if video.id == v_id:
            return video

def get_all_videos() -> list:
    return videos

def increase_views(v_id: str):
    video = find_by_id(v_id)
    video.views += 1

def convert_to_dict(v_id: str) -> dict:
    video = find_by_id(v_id)
    return_dict = {
        "id": video.id,
        "thumbnail": video.thumbnail,
        "extension": video.extension,
        "title": video.title,
        "author": video.author,
        "date_posted": video.date_posted,
        "views": video.views,
        "likes": video.likes,
        "dislikes": video.dislikes,
        "tags": video.tags,
        "comments": video.comments
    }
    return return_dict

def get_videos_with_tag(tag_name):
    videos_with_tag = []
    for video in videos:
        if tag_name in video.tags:
            videos_with_tag.append(video)
    return videos_with_tag