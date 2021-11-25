from fastapi import APIRouter, HTTPException

from api.updatedevice.models.battery_level import DeviceBatteryInfo
from api.utils.exceptions import KeyExistsError
from api.utils.response import ResponsePacket, build_response, ServiceCode
from database.shared_cache import update_device_battery_info

router = APIRouter()


@router.put('/battery_level_update', response_model=ResponsePacket)
def update_battery_info(battery_info: DeviceBatteryInfo):
    try:
        update_device_battery_info(battery_info)
    except KeyExistsError:
        raise HTTPException(status_code=400,
                            detail=build_response(ServiceCode.BATTERY_LEVEL_ERROR,
                                                  'Device Does Not Exists!').dict())

    return build_response(ServiceCode.BATTERY_LEVEL_RECEIVED)
