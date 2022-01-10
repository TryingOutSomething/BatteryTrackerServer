import os
from os.path import abspath, join, dirname
from socket import gethostname, gethostbyname_ex
from threading import Thread

from dotenv import load_dotenv
from pyngrok import ngrok

from api import start_api_server
from gui import start_gui

dotenv_path: str = abspath(join(dirname(__file__), '.env'))
load_dotenv(dotenv_path)

if __name__ == '__main__':
    USE_NGROK: bool = os.getenv('USE_NGROK', default='False') == 'True'

    device_ip_address = gethostbyname_ex(gethostname())[-1][-1]
    server_port = 8000

    if USE_NGROK:
        public_url = ngrok.connect(server_port, bind_tls=True).public_url
        print(f'NGROK: \tLocal endpoint proxied to endpoint: {public_url} successfully')
    else:
        public_url = f'{device_ip_address}:{server_port}'

    Thread(target=start_api_server, daemon=True, args=('0.0.0.0', server_port,)).start()
    start_gui(public_url)
