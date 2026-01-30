import re
from utils import call_log

class User:
    def __init__(self, raw: dict):
        self.id = raw.get("id")
        self.name = raw.get("name")
        self.email = raw.get("email")
        self.city = raw.get("address", {}).get("city")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": {"city": self.city}
        }
            
    def __str__(self):
        return f"User ({self.id} | {self.name} | {self.email} | {self.city})"
    
    
class UserAnalyzer:
    def __init__(self, users):
        self.users = users
    
    @call_log    
    def search(self, pattern):
        found = []
        
        for user in self.users:
            if (
                re.search(pattern, user.name, re.I)
                or re.search(pattern, user.email, re.I)
                or re.search(pattern, user.city, re.I)
            ):
                found.append(user)               
        
        return found
  
 