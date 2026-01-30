import json
from models import User
from utils import call_log


class Storage:
    def __init__(self, filename="src/users_data.json"):
        self.filename = filename    
    
    @call_log   
    def save(self, users):
        prepared = []
        
        for user in users:
                prepared.append(user.to_dict())
        
        try:
            with open(self.filename, "w", encoding='utf-8') as f:
                json.dump(prepared, f, ensure_ascii=False, indent=4)
        
        except FileNotFoundError:
            print("File not found")        
    
    @call_log    
    def load(self):
        try:
            with open(self.filename, "r", encoding='utf-8') as f:
                data = json.load(f)
            
            users = []
            
            for raw in data:
                users.append(User(raw))
            return users
        
        except Exception as e:
            print(f"Load error: {e}")
            return []
    
