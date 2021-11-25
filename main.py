from threading import Thread

import uvicorn

from api import get_api_server
from gui import start_gui

api_app = get_api_server()


def start_api_server():
    uvicorn.run('main:api_app')


if __name__ == '__main__':
    Thread(target=start_api_server, daemon=True).start()
    start_gui()
