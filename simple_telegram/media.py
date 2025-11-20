import requests


class _Media:
    def __init__(self, api_key: str):
        self._api_key: str = api_key

    def _get_file_path(self, file_id: str | None) -> str | None:
        if not file_id:
            return None

        url = f"https://api.telegram.org/bot{self._api_key}/getFile"
        try:
            r = requests.get(url, params={"file_id": file_id})
            data = r.json()
            if not data.get("ok"):
                return None
            return data["result"]["file_path"]
        except:
            return None

    def download(self, file_id: str | None) -> bytes | None:
        file_path = self._get_file_path(file_id)
        if not file_path:
            return None

        url = f"https://api.telegram.org/file/bot{self._api_key}/{file_path}"
        try:
            return requests.get(url).content
        except:
            return None


class Medias:
    def __init__(self, photo_data: list | None, video_data: dict | None, api_key: str):
        self.photos: list = []
        self.video: Video | None = None

        if isinstance(photo_data, list):
            for p in photo_data:
                if isinstance(p, dict):
                    self.photos.append(Photo(p, api_key))

        if isinstance(video_data, dict):
            self.video = Video(video_data, api_key)


class Photo(_Media):
    def __init__(self, data: dict, api_key: str):
        super().__init__(api_key)
        self.file_id: str | None = data.get("file_id")
        self.file_unique_id: str | None = data.get("file_unique_id")
        self.file_size: int | None = data.get("file_size")
        self.width: int | None = data.get("width")
        self.height: int | None = data.get("height")


class Video(_Media):
    def __init__(self, data: dict, api_key: str):
        super().__init__(api_key)
        self.file_id: str | None = data.get("file_id")
        self.file_unique_id: str | None = data.get("file_unique_id")
        self.file_size: int | None = data.get("file_size")
        self.width: int | None = data.get("width")
        self.height: int | None = data.get("height")
        self.duration: int | None = data.get("duration")
        self.mime_type: str | None = data.get("mime_type")
