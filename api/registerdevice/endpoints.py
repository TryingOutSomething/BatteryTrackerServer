from fastapi import APIRouter, HTTPException

from api.registerdevice.models.device import Device, UnregisterDevice
from api.utils.exceptions import KeyExistsError
from api.utils.response import ResponsePacket, build_response, ServiceCode
from database.shared_cache import register_device, unregister_device

router = APIRouter()


@router.post('/register', status_code=201, response_model=ResponsePacket)
def register_device_service(device: Device):
    try:
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
