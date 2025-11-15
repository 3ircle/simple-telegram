class Message :
    def __init__(self,message_data:dict,api_key):
        self._api_key = api_key
        self._message_data = message_data
        {'message_id': 16, 'from': {'id': 1891685872, 'is_bot': False, 'first_name': 'ali', 'last_name': 'momenzadeh', 'username': 'X_3ircle', 'language_code': 'en'}, 'chat': {'id': 1891685872, 'first_name': 'ali', 'last_name': 'momenzadeh', 'username': 'X_3ircle', 'type': 'private'}, 'date': 1762761592, 'photo': [{'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAANzAAM2BA', 'file_unique_id': 'AQADCwtrG52YkVB4', 'file_size': 950, 'width': 51, 'height': 90}, {'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAANtAAM2BA', 'file_unique_id': 'AQADCwtrG52YkVBy', 'file_size': 13141, 'width': 180, 'height': 320}, {'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAAN4AAM2BA', 'file_unique_id': 'AQADCwtrG52YkVB9', 'file_size': 63871, 'width': 450, 'height': 800}, {'file_id': 'AgACAgQAAxkBAAMQaRGbeOWbq4IFbeAV1mvUH8vfOlEAAgsLaxudmJFQyn6oYecv394BAAMCAAN5AAM2BA', 'file_unique_id': 'AQADCwtrG52YkVB-', 'file_size': 129159, 'width': 720, 'height': 1280}]}
        self.message_id :int = self._message_data.get('message_id',-1)
        self._user : dict = self._message_data.get('user',{})
        self._chat :dict = self._message_data.get('chat',{})
        self._photo : dict = self._message_data.get('photo',{})
        self.date : int = self._message_data.get('date',0)
        self.text :str = self._message_data.get('text','')

    def reply(self):
        pass

