from .user import User


class Chat:
    def __init__(self, data: dict, api_key: str):
        self._api_key: str = api_key
        self._data: dict = data or {}

        self.id: int = self._data.get("id", 0)
        self.type: str = self._data.get("type", "")
        self.title: str = self._data.get("title", "")
        self.accepted_gift_types = self._data.get("accepted_gift_types", {})

        new = self._data.get("new_chat_member", {})
        self.new_chat_member: User | None = (
            User(new, api_key) if isinstance(new, dict) else None
        )
