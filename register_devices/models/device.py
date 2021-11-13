from pydantic import BaseModel, validator

from utils import request_payload_validators as req_validators
from utils.response import ServiceCode


class Device(BaseModel):
    device_id: str
    device_name: str
    battery_level: str

    @validator('*')
    def empty_fields(cls, v):
        if req_validators.is_empty_field(v):
            raise ValueError(ServiceCode.FIELD_EMPTY.value)

        return v

    @validator('battery_level')
    def is_valid_battery_level(cls, v):
        is_valid_value = req_validators.is_within_valid_battery_range(v)

        if not is_valid_value:
            raise ValueError(ServiceCode.INVALID_BATTERY_RANGE.value)

        return v


class UnregisterDevice(BaseModel):
    device_id: str
