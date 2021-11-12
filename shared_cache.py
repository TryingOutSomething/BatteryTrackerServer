import threading
from typing import Dict, Optional

from battery_info.models.battery_level import BatteryInfo
from register_devices.models.device import Device, UnregisterDevice
from utils.exceptions import KeyExistsError

_REGISTERED_DEVICE_NAME_KEY = 'name'
_REGISTERED_DEVICE_BATTERY_LEVEL_KEY = 'battery_level'

_registered_devices: Dict[str, Dict[str, str]] = {}
_lock: threading.Lock = threading.Lock()


def register_device(device: 'Device') -> None:
    with _lock:
        if _device_exists(device.device_id):
            raise KeyExistsError('Device already exists in memory')

        device_id = device.device_id
        device_name = device.device_name
        battery_level = device.battery_level

        _registered_devices[device_id] = {
            _REGISTERED_DEVICE_NAME_KEY: device_name,
            _REGISTERED_DEVICE_BATTERY_LEVEL_KEY: battery_level
        }


def _device_exists(device_id: str) -> bool:
    return device_id in _registered_devices


def unregister_device(device: 'UnregisterDevice') -> Optional[Dict[str, str]]:
    with _lock:
        return _registered_devices.pop(device.device_imei, None)


def update_device_battery_info(device_battery_info: 'BatteryInfo') -> None:
    with _lock:
        if not _device_exists(device_battery_info.device_id):
            raise KeyExistsError('Device does not exist in memory')

        device_id = device_battery_info.device_id
        battery_level = device_battery_info.current_battery_level

        _registered_devices[device_id][_REGISTERED_DEVICE_BATTERY_LEVEL_KEY] = battery_level


def get_all_registered_devices():
    ...
