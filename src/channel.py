import json
import os
from googleapiclient.discovery import build
import isodate

class Channel:
    """Класс для ютуб-канала"""
    api_key = "AIzaSyCmOygzhlZwoIzxmKzigRrFcJhE3Z3srhQ"
    # api_key = os.getenv('YT_API_KEY'))

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        if type(channel_id) is not str:
            raise ValueError("Значение должно быть типа строка")
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_info = print(json.dumps(channel, indent=2, ensure_ascii=False))
        return channel_info
