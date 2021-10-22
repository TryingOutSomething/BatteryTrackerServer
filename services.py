from typing import Optional

from utils.exceptions import KeyExistsError
from battery_info.models.battery_level import BatteryInfo
from register_devices.models.device import Device, UnregisterDevice

_registered_devices = {}


def register_device(device: Device) -> None:
    if _device_exists(device.device_imei):
        raise KeyExistsError('Key already exists')

    imei = device.device_imei
    name = device.device_name
    battery_level = device.battery_level

    _registered_devices[imei] = {
        'name': name,
        'battery_level': battery_level
    }


def unregister_device(device: UnregisterDevice) -> Optional[Device]:
    return _registered_devices.pop(device.device_imei, None)


def _device_exists(imei_number) -> bool:
    return imei_number in _registered_devices


def update_device_battery_info(battery_info: BatteryInfo) -> None:
    if not _device_exists(battery_info.device_imei):
        raise KeyExistsError('key already exists')

    imei = battery_info.device_imei
    battery_level = battery_info.current_battery_level

    _registered_devices[imei] = battery_level
