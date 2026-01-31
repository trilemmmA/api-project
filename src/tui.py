from models import User, UserAnalyzer
from storage import *
from rich.console import Console
from rich.table import Table

class App:
    def __init__(self, client, storage):
        self.client = client
        self.storage = storage
        self.users = []
        self.analyzer = UserAnalyzer(self.users)
        self.console = Console()
        
    def load_users(self):
        raw = self.client.fetch_users()
        
        self.users = [User(u) for u in raw]
        self.analyzer = UserAnalyzer(self.users)
        return self.analyzer
 
    def show_menu(self):
        self.console.rule("[bold cyan]Analyzer[/bold cyan]")
        
        self.console.print("[bold]1[/bold] - Load Users")
        self.console.print("[bold]2[/bold] - Search")
        self.console.print("[bold]3[/bold] - Show all")
        self.console.print("[bold]4[/bold] - Exit")
    
    def show_rich(self, users):
        table = Table(title="Users")
        
        table.add_column("ID")
        table.add_column("Name")
        table.add_column("Email")
        table.add_column("City")
        
        for user in users:
            table.add_row(str(user.id), user.name, user.email, user.city)
            
        self.console.print(table)
        
    def handle_choice(self):
        self.show_menu()
        while True:
            choice = input("Choose: ")
            
            if choice == "1":
                self.load_users()
                print(f"Loaded {len(self.users)} users")
            
            elif choice == "2":            
                if not self.users:
                    self.console.print("[yellow]Load users first[/yellow]")
                    continue
                
                pattern = input("Enter search pattern: ")
            
                result = self.analyzer.search(pattern)            
                       
                self.show_rich(result)
                
                self.storage.save(result)
                                            
            elif choice == "3":
                saved_data = self.storage.load()
            
                if not saved_data:
                    self.console.print("[bold red]History is empty[/bold red]", justify="center")
                
                self.show_rich(saved_data)
            
            elif choice == "4":
                break
            
            else:
                print("Wrong command")
            
    def run(self):
        self.handle_choice()
            
