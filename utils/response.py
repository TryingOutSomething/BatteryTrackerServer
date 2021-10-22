from enum import Enum

from pydantic import BaseModel


class _StrEnum(str, Enum):
    pass


class ServiceCode(_StrEnum):
    # Success codes
    REGISTER_SUCCESS = '100'
    UNREGISTER_SUCCESS = '110'
    BATTERY_LEVEL_RECEIVED = '120'

    # Error Codes
    REGISTER_FAILURE = '200'
    UNREGISTER_FAILURE = '210'
    BATTERY_LEVEL_ERROR = '220'
    PARAMETER_VALIDATION_ERROR = '230'
    FIELD_EMPTY = '231'
    INVALID_BATTERY_RANGE = '232'


class ResponsePacket(BaseModel):
    service_code: ServiceCode
    message: str


def build_response(code: ServiceCode, message: str = '') -> ResponsePacket:
    payload = {'service_code': code, 'message': message}
    return ResponsePacket(**payload)
