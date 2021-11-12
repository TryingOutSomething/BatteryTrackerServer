from fastapi import APIRouter, HTTPException

from register_devices.models.device import Device, UnregisterDevice
from shared_cache import register_device, unregister_device
from utils.exceptions import KeyExistsError
from utils.response import ResponsePacket, build_response, ServiceCode

router = APIRouter()


@router.post('/register', status_code=201, response_model=ResponsePacket)
def register_device_service(device: Device):
    try:
        register_device(device)
    except KeyExistsError:
        raise HTTPException(status_code=400,
                            detail=build_response(ServiceCode.REGISTER_FAILURE,
                                                  'Device Already Exists!'))

    return build_response(ServiceCode.REGISTER_SUCCESS)


@router.delete('/unregister', response_model=ResponsePacket)
def unregister_device_service(device: UnregisterDevice):
    device_info = unregister_device(device)

    if device_info is None:
        raise HTTPException(status_code=400,
                            detail=build_response(ServiceCode.UNREGISTER_FAILURE,
                                                  'Device Does Not Exists!'))

    return build_response(ServiceCode.UNREGISTER_SUCCESS)
