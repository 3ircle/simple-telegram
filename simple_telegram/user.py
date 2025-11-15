class User :
    def __init__(self,user_data:dict,api_key:str):
        self._api_key : str = api_key
        self._user_data : dict = user_data
        self.id = self._user_data.get('id',0)
        self.is_bot = self._user_data.get('is_bot',False)
        self.first_name : str = self._user_data.get('first_name','')
        self.last_name : str = self._user_data.get('last_name','')
        self.username : str = self._user_data.get('username','')
    
    def send_message(self):
        pass
