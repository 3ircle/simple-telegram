# bot.py
import requests
import json
from .update import Update
from .configs import PROXY


class Bot:
    def __init__(self, api_key: str):
        self.api_key: str = api_key
        self._base_url: str = f'https://api.telegram.org/bot{self.api_key}/'
        self.message_handler = None
        self.command_handler = None
        self._last_offset: int = 0

    def _send_message(self, message: str, user_id: int) -> bool:
        url = self._base_url + "sendMessage"
        payload = {"chat_id": user_id, "text": message}
        try:
            res = requests.post(url, data=payload, proxies=PROXY)
            return res.status_code == 200
        except Exception:
            return False

    def _send_image(self, image: bytes, user_id: int) -> bool:
        url = self._base_url + "sendPhoto"
        files = {"photo": image}
        data = {"chat_id": user_id}
        try:
            res = requests.post(url, data=data, files=files, proxies=PROXY)
            return res.status_code == 200
        except Exception:
            return False

    def _send_video(self, video: bytes, user_id: int) -> bool:
        url = self._base_url + "sendVideo"
        files = {"video": video}
        data = {"chat_id": user_id}
        try:
            res = requests.post(url, data=data, files=files, proxies=PROXY)
            return res.status_code == 200
        except Exception:
            return False

    def _get_update(self) -> Update:
        update_url = self._base_url + "getUpdates?offset=" + str(self._last_offset)
        try:
            req = requests.get(update_url, proxies=PROXY, timeout=10)
            if req.status_code == 200:
                data = json.loads(req.content)
                update_obj = Update(data, self.api_key) if data.get("ok") else Update({})
                if update_obj.message:
                    self._last_offset = data["result"][-1]["update_id"] + 1
                return update_obj
            return Update({})
        except Exception:
            return Update({})

    def run(self, time_out: int = 10):
        import time
        print('the robot is running')

        while True:
            update = self._get_update()
            if not update.message:
                time.sleep(time_out)
                continue

            # فرمان‌ها
            if update.type == "command" and self.command_handler:
                self.command_handler(update)
            # پیام‌ها
            elif update.type == "message" and self.message_handler:
                self.message_handler(update)

            time.sleep(time_out)
