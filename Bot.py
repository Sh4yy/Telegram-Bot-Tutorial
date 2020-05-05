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
        result = result.json()['result']
        
        print(f'This is {result["username"]}')
        return result
    
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
        
        result.raise_for_status()
        pprint(result)
        
    def get_updates(self, offset=None, limit=10, timeout=5):
        """
        used to receive updates using long polling
        :param offset: starting update id
        :param limit: number of results
        :param timeout: long polling timeout (sec)
        :return: [Updates]
        """
        
        params = {
            'limit': limit,
            'timeout': timeout
        }
        
        if offset is not None:
            params['offset'] = offset
        
        result = self._get_request(
            method='getUpdates',
            params=params,
            timeout=timeout + 1
        )
        
        result.raise_for_status()
        return result.json().get('result')
    
    def _get_request(self, method, params=None, timeout=5):
        
        url = self._base_url + method
        return requests.get(
            url=url,
            params=params,
            timeout=timeout
        )
    
    def _post_request(self, method, params=None):
        
        url = self._base_url + method
        return requests.post(
            url=url,
            params=params
        )
        

class UpdateHandler:

    def __init__(self, bot, timeout=5):
        self._bot = bot
        self._callback = None
        self._offset = None
        self._timeout = timeout
        
    def register(self, callback):
        """ register a new callback function """
        self._callback = callback
    
    def start_polling(self):    
        while True:
            self._long_poll()
            
    def _long_poll(self):
        
        updates = self._bot.get_updates(
            offset=self._offset,
            timeout=self._timeout
        )
        
        for update in updates:
            self._callback(update)
            self._offset = update['update_id'] + 1
            
    