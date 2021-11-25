import threading
from typing import Dict, Optional

from api.registerdevice.models.device import Device, UnregisterDevice
from api.updatedevice.models.battery_level import DeviceBatteryInfo
from api.utils.exceptions import KeyExistsError

_registered_devices: Dict[str, 'Device'] = {}
_lock: threading.Lock = threading.Lock()


def _device_exists(device_id: str) -> bool:
    return device_id in _registered_devices


def register_device(device: 'Device') -> None:
    with _lock:
        if _device_exists(device.device_id):
            raise KeyExistsError('Device already exists in memory')

        device_id = device.device_id
        _registered_devices[device_id] = device


def unregister_device(device: 'UnregisterDevice') -> Optional[Dict[str, str]]:
    with _lock:
        return _registered_devices.pop(device.device_id, None)


def update_device_battery_info(device_battery_info: 'DeviceBatteryInfo') -> None:
    with _lock:
        if not _device_exists(device_battery_info.device_id):
            raise KeyExistsError('Device does not exist in memory')

        device_id = device_battery_info.device_id
        battery_level = device_battery_info.current_battery_level

        _registered_devices[device_id].battery_level = battery_level


def get_all_registered_devices() -> Dict[str, 'Device']:
    return _registered_devices
