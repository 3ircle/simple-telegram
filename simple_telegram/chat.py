from .user import User

class Chat :
    def __init__(self,chat_data,api_key):
        self._api_key : str = api_key
        self._chat_data : dict = chat_data
        self.accepted_gift_types : dict = self._chat_data.get('accepted_gift_types',{})
        self.id : int = self._chat_data.get('id',0)
        self.type : str = self._chat_data.get('type','')
        self.title : str = self._chat_data.get('title','')
        self.all_members_are_administrators : bool = self._chat_data.get('all_members_are_administrators',False)
        self.new_chat_member : User = User(self._chat_data.get('new_chat_member',{}),self._api_key)

