from models import User, UserAnalyzer
from storage import *

class App:
    def __init__(self, client, storage):
        self.client = client
        self.storage = storage
        self.users = []
        self.analyzer = UserAnalyzer(self.users)
        
    def load_users(self):
        raw = self.client.fetch_users()
        
        self.users = [User(u) for u in raw]
        self.analyzer = UserAnalyzer(self.users)
        return self.analyzer
 
    def show_menu(self):
        print("\nMenu")
        print("1 - Load Users")
        print("2 - Search")
        print("3 - Show all")
        print("4 - Exit")
        
    def handle_choice(self):
        self.show_menu()
        while True:
            choice = input("Choose: ")
            
            if choice == "1":
                self.load_users()
                print(f"Loaded {len(self.users)} users")
            
            elif choice == "2":            
                if not self.users:
                    print("Load users first")
                    continue
                
                pattern = input("Enter search pattern: ")
            
                result = self.analyzer.search(pattern)            
                       
                for user in result:
                    print(user)
                
                self.storage.save(result)
                                            
            elif choice == "3":
                saved_data = self.storage.load()
            
                if not saved_data:
                    print("History is empty")
                
                for user in saved_data:
                    print(user)
            
            elif choice == "4":
                break
            
    def run(self):
        self.handle_choice()
            
