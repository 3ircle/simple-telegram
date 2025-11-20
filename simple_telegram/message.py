import requests
from .chat import Chat
from .media import Medias


class Message:
    def __init__(self, data: dict, api_key: str):
        self._data: dict = data or {}
        self._api_key: str = api_key

        self.message_id: int = self._data.get("message_id", -1)
        self.text: str = self._data.get("text", "")
        self.date: int = self._data.get("date", 0)

        self.chat: Chat = Chat(self._data.get("chat", {}), api_key)
        self.from_user = self._data.get("from", {})

        media_photo = self._data.get("photo")
        media_video = self._data.get("video")
        self.media = Medias(media_photo, media_video, api_key)

    def reply(self, text: str) -> bool:
        url = f"https://api.telegram.org/bot{self._api_key}/sendMessage"
        payload = {
            "chat_id": self.chat.id,
            "text": text,
            "reply_to_message_id": self.message_id
        }
        try:
            r = requests.post(url, json=payload)
            data = r.json()
            return data.get("ok", False)
        except:
            return False
