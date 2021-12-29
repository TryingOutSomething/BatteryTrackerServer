from fastapi import APIRouter, HTTPException

from api.exceptions import KeyExistsError
from api.payload_validators import is_empty_field, is_within_valid_battery_range
from api.updatedevice.models.battery_level import DeviceBatteryInfo
from api.utils.response import ResponsePacket, build_response, ServiceCode
from database.shared_cache import update_device_battery_info

router = APIRouter()


@router.put('/update', response_model=ResponsePacket)
def update_battery_info(battery_info: DeviceBatteryInfo):
    try:
        if is_empty_field(battery_info.device_id) or is_empty_field(battery_info.current_battery_level):
            raise HTTPException(status_code=422,
                                detail=build_response(ServiceCode.FIELD_EMPTY,
                                                      'Missing Parameters!').dict())

        if not is_within_valid_battery_range(battery_info.current_battery_level):
            raise HTTPException(status_code=422,
                                detail=build_response(ServiceCode.INVALID_BATTERY_RANGE,
                                                      'Invalid Battery Range!').dict())
        update_device_battery_info(battery_info)
    except KeyExistsError:
        raise HTTPException(status_code=400,
                            detail=build_response(ServiceCode.BATTERY_LEVEL_ERROR,
                                                  'Device Does Not Exists!').dict())

    return build_response(ServiceCode.BATTERY_LEVEL_RECEIVED)
