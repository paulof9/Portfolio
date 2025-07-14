import requests
import json

class ReposList:
    def __init__(self, username):
        self._username = username

    def req_api(self):
        res = requests.get(f'https://api.github.com/users/{self._username}/repos')
        if res.status_code == 200:
            return res.json()
        else:
            return []

    def get_repos(self):
        data_api = self.req_api()
        filter = [repo for repo in data_api if repo.get('language') is not None]
        return filter
    
    def req_api_user(self):
        res = requests.get(f'https://api.github.com/users/{self._username}')
        if res.status_code == 200:
            return res.json()
        else:
            return {}
        
    def get_user(self):
        data_api = self.req_api_user()
        return data_api
