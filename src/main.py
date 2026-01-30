from tui import App
from clients import APIClient
from storage import Storage

def main():
    client = APIClient("https://jsonplaceholder.typicode.com/users")
    storage = Storage()
    app = App(client, storage)
    app.run()

if __name__ == "__main__":
    main()
