import requests
from pprint import pprint


class Bot:
    
    def __init__(self, token):
        self._token = token
        self._base_url = f"https://api.telegram.org/bot{token}/"
        
    def get_me(self):
        """ test bot's auth token """
        
        result = self._get_request(
            method='getMe'
        )
        
        result.raise_for_status()
        return result.json()['result']
    
    def send_message(self, chat_id, text):
        """
        send a message to a user on telegram
        :param chat_id: unique identifier for our target
        :param text: string message
        """
        
        result = self._post_request(
            method='sendMessage',
            params={
                'chat_id': chat_id,
                'text': text
            }
        )
        
        pprint(result)
    
    def _get_request(self, method):
        
        url = self._base_url + method
        return requests.get(url=url)
    
    def _post_request(self, method, params=None):
        
        url = self._base_url + method
        return requests.post(url=url, params=params)
        