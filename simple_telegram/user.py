import requests


class User:
    def __init__(self, data: dict, api_key: str):
        self._api_key: str = api_key
        self._data: dict = data or {}

        self.id: int = self._data.get("id", 0)
        self.is_bot: bool = self._data.get("is_bot", False)
        self.first_name: str = self._data.get("first_name", "")
        self.last_name: str = self._data.get("last_name", "")
        self.username: str = self._data.get("username", "")

    def send_message(self, text: str) -> bool:
        url = f"https://api.telegram.org/bot{self._api_key}/sendMessage"
        payload = {"chat_id": self.id, "text": text}
        try:
            r = requests.post(url, json=payload)
            data = r.json()
            return data.get("ok", False)
        except:
            return False
