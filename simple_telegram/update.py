from .user import User
from .media import Photo
from .message import Message

class Update:
    def __init__(self, update_json: dict, api_key):
        {'ok': True, 'result': [{'update_id': 80934383, 'message': {'message_id': 16, 'from': {'id': 1891685872, 'is_bot': False, 'first_name': 'ali', 'last_name': 'momenzadeh', 'username': 'X_3ircle', 'language_code': 'en'}, 'chat': {'id': 1891685872, 'first_name': 'ali', 'last_name': 'momenzadeh', 'username': 'X_3ircle', 'type': 'private'}, 'date': 1762761592, 'photo': [{'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAANzAAM2BA', 'file_unique_id': 'AQADCwtrG52YkVB4', 'file_size': 950, 'width': 51, 'height': 90}, {'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAANtAAM2BA', 'file_unique_id': 'AQADCwtrG52YkVBy', 'file_size': 13141, 'width': 180, 'height': 320}, {'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAAN4AAM2BA', 'file_unique_id': 'AQADCwtrG52YkVB9', 'file_size': 63871, 'width': 450, 'height': 800}, {'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAAN5AAM2BA', 'file_unique_id': 'AQADCwtrG52YkVB-', 'file_size': 129159, 'width': 720, 'height': 1280}]}}]}
        self._api_key : str = api_key
        self._update_json : dict = update_json
        self.update_id : int = self._update_json.get('result',[{}])[-1].get('update_id')
        self.ok : bool = self._update_json.get('ok',False)
        self._message : dict = self._update_json.get('result',[{}])[-1].get('message')
        self.message : Message = Message(self._message,self._api_key)









