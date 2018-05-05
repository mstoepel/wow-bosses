import requests

class Wow:
    def __init__(self):
        self.api_key = 'h2dujjpu5aea5999kffnjddsvxjdssrp'

    def get_boss(self, id):
        url = 'https://us.api.battle.net/wow/boss/{id}?locale=en_US&apikey={api_key}'
        info = {'id': id, 'api_key': self.api_key}

        return requests.get(url.format(**info)).json()

    def get_all_bosses(self):
        url = 'https://us.api.battle.net/wow/boss/?locale=en_US&apikey={api_key}'
        info = {'api_key': self.api_key}

        return requests.get(url.format(**info)).json()['bosses']



