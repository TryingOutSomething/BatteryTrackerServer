from threading import Thread

import uvicorn

from api import get_api_server
from gui import start_gui
from gui.notifications import notify_device_charged

api_app = get_api_server()


def start_api_server():
    uvicorn.run('main:api_app')


if __name__ == '__main__':
    Thread(target=start_api_server, daemon=True).start()
    start_gui()
    notify_device_charged('hi', 'test')
