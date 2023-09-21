import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            return None

    def load_json(self):
        response_content = self.get_response_body()
        if response_content:
            return json.loads(response_content)
        else:
            return None