from fastapi import APIRouter, HTTPException

from battery_info.models.battery_level import BatteryInfo
from shared_cache import update_device_battery_info
from utils.exceptions import KeyExistsError
from utils.response import ResponsePacket, build_response, ServiceCode

router = APIRouter()


@router.post('/battery', response_model=ResponsePacket)
def receive_battery_info(battery_info: BatteryInfo):
    try:
        update_device_battery_info(battery_info)
    except KeyExistsError:
        raise HTTPException(status_code=400,
                            detail=build_response(ServiceCode.BATTERY_LEVEL_ERROR,
                                                  'Device Does Not Exists!').dict())

    return build_response(ServiceCode.BATTERY_LEVEL_RECEIVED)
