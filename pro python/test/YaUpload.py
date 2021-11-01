import requests

class YaUpload:
    def __init__(self, token):
        self.API_BASE_URL = "https://cloud-api.yandex.net/"
        self.token = token
        self.headers = {
            'accept': 'application/json' ,
            'authorization': f'OAuth {self.token}'
        }

    def upload_dir(self, path):
        response = requests.put(self.API_BASE_URL + "v1/disk/resources",\
             headers=self.headers, params={"path":path})
        return response




