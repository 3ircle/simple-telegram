class Media :
    def __init__(self,api_key):
        self._api_key = api_key
    def download(self):
        pass


class Photo(Media):
    def __init__(self,photo,api_key):
        super().__init__(api_key)
        self.file_id = photo.get('file_id')
        self.file_unique_id = photo.get('file_unique_id')
        self.file_size = photo.get('file_size')
        self.width = photo.get('width')
        self.height = photo.get('height')


