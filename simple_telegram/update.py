from .message import Message


class Update:
    def __init__(self, update_json: dict, api_key: str):
        self._json: dict = update_json
        self._api_key: str = api_key

        result = self._json.get("result", [])
        last = result[-1] if result else {}
        message_data = last.get("message")

        if isinstance(message_data, dict):
            self.message = Message(message_data, api_key)
        else:
            self.message = None

        self.type: str | None = None
        self.args: list | None = None
        self.command: str | None = None

        if self.message and isinstance(self.message.text, str):
            txt = self.message.text.strip()

            if txt.startswith("/"):
                self.type = "command"
                parts = txt.split()
                self.command = parts[0]
                self.args = parts
            else:
                self.type = "message"
