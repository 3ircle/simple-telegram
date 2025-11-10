import requests
import json
from .update import Update
from .configs import PROXY 

class Bot :
    def __init__(self,api_key):
        self.api_key = api_key
        self._base_url = f'https://api.telegram.org/bot{self.api_key}/'
        self.message_handler = None
        self.command_handler = None
        self._last_offset = 0

    def _send_message(self,message:str,user_id):
        pass

    def _send_image(self,image:bytes,user_id):
        pass

    def _send_video(self,video:bytes,user_id):
        pass

    def _get_update(self) -> Update :
        update_url = self._base_url + 'getUpdates?offset=' + str(self._last_offset)
        req = requests.get(update_url,proxies=PROXY)
        if req.status_code == 200:
            data = json.loads(req.content)
            return Update(data,self.api_key) if data.get('ok') else Update({})
        else :
            return {}



    def run(self,time_out=10):
        pass

