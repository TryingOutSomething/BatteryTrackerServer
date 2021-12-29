from typing import List, Dict, Any

import uvicorn
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

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


@_app.exception_handler(RequestValidationError)
def validation_exception_handler(_: Request, exc: RequestValidationError):
    error_service_codes_string = compile_error_service_codes(exc.errors())

    return JSONResponse(status_code=422,
                        content=jsonable_encoder(
                            build_response(ServiceCode.PARAMETER_VALIDATION_ERROR,
                                           error_service_codes_string)
                        ))


def compile_error_service_codes(list_of_errors: List[Dict[str, Any]]) -> str:
    error_service_codes_set = {error['msg'] for error in list_of_errors}
    return ','.join(error_service_codes_set)


def start_api_server():
    uvicorn.run('main:api_app')
