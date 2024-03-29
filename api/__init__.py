import uvicorn
from fastapi import FastAPI

from .registerdevice.endpoints import router as device_router
from .updatedevice.endpoints import router as battery_info_router
from .utils.response import build_response, ServiceCode

_app = FastAPI()
_app.include_router(
    battery_info_router,
    prefix='/battery_level',
    tags=['Receive Battery Level']
)

_app.include_router(
    device_router,
    prefix='/device',
    tags=['Register & Unregister Device']
)


def start_api_server(host='0.0.0.0', port=8000):
    uvicorn.run('api:_app', host=host, port=port, log_level='info')
