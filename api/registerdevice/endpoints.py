from fastapi import APIRouter, HTTPException

from api.exceptions import KeyExistsError
from api.payload_validators import is_empty_field, is_within_valid_battery_range
from api.registerdevice.models.device import Device, UnregisterDevice
from api.utils.response import ResponsePacket, build_response, ServiceCode
from database.shared_cache import register_device, unregister_device

router = APIRouter()


@router.post('/register', status_code=201, response_model=ResponsePacket)
def register_device_service(device: Device):
    try:
        if is_empty_field(device.device_id) or is_empty_field(device.device_name) or is_empty_field(
                device.battery_level):
            raise HTTPException(status_code=422,
                                detail=build_response(ServiceCode.FIELD_EMPTY,
                                                      'Missing Parameters!').dict())

        if not is_within_valid_battery_range(device.battery_level):
            raise HTTPException(status_code=422,
                                detail=build_response(ServiceCode.INVALID_BATTERY_RANGE,
                                                      'Invalid Battery Range!').dict())

        register_device(device)
    except KeyExistsError:
        raise HTTPException(status_code=400,
                            detail=build_response(ServiceCode.REGISTER_FAILURE,
                                                  'Device Already Exists!').dict())

    return build_response(ServiceCode.REGISTER_SUCCESS)


@router.delete('/unregister', response_model=ResponsePacket)
def unregister_device_service(device: UnregisterDevice):
    device_info = unregister_device(device)

    if device_info is None:
        raise HTTPException(status_code=400,
                            detail=build_response(ServiceCode.UNREGISTER_FAILURE,
                                                  'Device Does Not Exists!').dict())

    return build_response(ServiceCode.UNREGISTER_SUCCESS)
