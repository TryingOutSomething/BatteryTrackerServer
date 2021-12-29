from socket import gethostname, gethostbyname_ex
from threading import Thread

from api import start_api_server
from gui import start_gui

if __name__ == '__main__':
    device_ip_address = gethostbyname_ex(gethostname())[-1][-1]
    server_port = 8000

    Thread(target=start_api_server, daemon=True, args=('0.0.0.0', server_port,)).start()
    start_gui(device_ip_address, server_port)
