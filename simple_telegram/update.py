from .user import User
from .media import Photo


class Update:
    def __init__(self, update_json: dict, api_key):
        self._api_key = api_key
        self._update_json = update_json
        

        self.message_data = update_json.get('result')[-1] if update_json.get('result') else {}
        
        if self.message_data:
            self._from_data = self.message_data.get('from', {})
            

            self.user = User(
                self._from_data.get('id'),
                self._from_data.get('is_bot'),
                self._from_data.get('first_name'),
                self._from_data.get('last_name'),
                self._from_data.get('username'),
            )
            

            self.photo = [Photo(i, api_key=self._api_key) for i in self.message_data.get('photo', [])]
            

            self.text = self.message_data.get('text')
        else:
            self.user = None
            self.photo = []
            self.text = None


{'ok': True, 'result': [{'update_id': 80934383, 'message': {'message_id': 16, 'from': {'id': 1891685872, 'is_bot': False, 'first_name': 'ali', 'last_name': 'momenzadeh', 'username': 'X_3ircle', 'language_code': 'en'}, 'chat': {'id': 1891685872, 'first_name': 'ali', 'last_name': 'momenzadeh', 'username': 'X_3ircle', 'type': 'private'}, 'date': 1762761592, 'photo': [{'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAANzAAM2BA', 'file_unique_id': 'AQADCwtrG52YkVB4', 'file_size': 950, 'width': 51, 'height': 90}, {'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAANtAAM2BA', 'file_unique_id': 'AQADCwtrG52YkVBy', 'file_size': 13141, 'width': 180, 'height': 320}, {'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAAN4AAM2BA', 'file_unique_id': 'AQADCwtrG52YkVB9', 'file_size': 63871, 'width': 450, 'height': 800}, {'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAAN5AAM2BA', 'file_unique_id': 'AQADCwtrG52YkVB-', 'file_size': 129159, 'width': 720, 'height': 1280}]}}]}