import requests
from utils import call_log

class APIClient:
    def __init__(self, url):
        self.url = url    
    
    @call_log
    def fetch_users(self):
        response = requests.get(self.url, timeout=5)
        
        if response.status_code != 200:
            print(f"Request failed: {response.status_code}")
            return[]
        return response.json()
    
        