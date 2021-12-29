from threading import Thread

from api import start_api_server
from gui import start_gui

if __name__ == '__main__':
    Thread(target=start_api_server, daemon=True, args=('0.0.0.0', 8000,)).start()
    start_gui()
