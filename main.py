from typing import List, Dict, Any

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from device_battery_info.endpoints import router as battery_info_router
from register_devices.endpoints import router as device_router
from utils.response import build_response, ServiceCode

app = FastAPI()
app.include_router(
    battery_info_router,
    prefix='/batteryLevel',
    tags=['Receive Battery Level']
)

app.include_router(
    device_router,
    prefix='/device',
    tags=['Register & Unregister Device']
)


@app.exception_handler(RequestValidationError)
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
