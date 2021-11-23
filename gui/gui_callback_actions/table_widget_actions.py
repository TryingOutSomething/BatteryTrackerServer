from enum import IntEnum
from typing import Dict

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from register_devices.models.device import Device


class BatteryLevelToNotify:
    def __init__(self, battery_level: int):
        self.battery_level_to_notify: int = battery_level
        self.has_notified: bool = False


class _DeviceTableRecord(IntEnum):
    DEVICE_NAME_COLUMN = 0
    BATTERY_LEVEL_COLUMN = 1
    BATTERY_LEVEL_TO_NOTIFY_COLUMN = 2
    DEFAULT_BATTERY_LEVEL_TO_NOTIFY = 80


def set_allow_only_last_column_editable(devices_list: QTableWidget) -> None:
    for row in range(devices_list.rowCount()):
        for col in range(devices_list.columnCount() - 1):
            _set_cell_as_immutable(devices_list.item(row, col))


def _set_cell_as_immutable(cell: QTableWidgetItem):
    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)


def sync_shared_cache_with_gui(devices_list: QTableWidget,
                               shared_cache_devices: Dict[str, Device],
                               table_row_id_device_map: Dict[int, str],
                               device_battery_level_to_notify_map: Dict[str, BatteryLevelToNotify]):
    no_of_devices_registered_in_gui: int = devices_list.rowCount()

    registered_devices_dict: Dict[str, Device] = \
        _get_new_registered_and_remove_unregistered_device(devices_list,
                                                           no_of_devices_registered_in_gui,
                                                           shared_cache_devices,
                                                           table_row_id_device_map,
                                                           device_battery_level_to_notify_map)

    _register_new_devices_to_gui(device_battery_level_to_notify_map,
                                 devices_list,
                                 registered_devices_dict,
                                 shared_cache_devices,
                                 table_row_id_device_map)


def _get_new_registered_and_remove_unregistered_device(devices_list: QTableWidget,
                                                       no_of_devices_registered_in_gui: int,
                                                       shared_cache_devices: Dict[str, Device],
                                                       table_row_id_device_map: Dict[int, str],
                                                       device_battery_to_notify_map: Dict[str, BatteryLevelToNotify]):
    registered_devices_dict: Dict[str, Device] = {}

    if no_of_devices_registered_in_gui <= 0:
        return registered_devices_dict

    for row_index in range(no_of_devices_registered_in_gui):
        device_id: str = table_row_id_device_map[row_index]

        if device_id not in shared_cache_devices:
            # remove entry from table widget
            _remove_new_registered_device_from_table(devices_list, row_index)
            table_row_id_device_map.pop(row_index)
            device_battery_to_notify_map.pop(device_id)
            continue

        registered_devices_dict[device_id] = shared_cache_devices[device_id]

        shared_cache_device_info: Device = shared_cache_devices[device_id]
        gui_device_battery_level: str = _get_device_battery_level_from_table(devices_list, row_index)

        if gui_device_battery_level == shared_cache_device_info.battery_level:
            continue

        updated_device_battery_level: str = str(shared_cache_device_info.battery_level)
        _update_device_battery_level_in_table(devices_list, row_index, updated_device_battery_level)

    return registered_devices_dict


def _register_new_devices_to_gui(device_battery_level_to_notify_map,
                                 devices_list,
                                 registered_devices_dict,
                                 shared_cache_devices,
                                 table_row_id_device_map):
    registered_devices_set: set = set(registered_devices_dict.items())
    shared_cache_device_id_set: set = set(shared_cache_devices.items())
    new_registered_devices_set: set = shared_cache_device_id_set - registered_devices_set

    for new_device_id, device in dict(new_registered_devices_set).items():
        # insert to table
        table_row_id = _insert_new_registered_device_to_table(devices_list, device)
        # update table row id to device id
        device_id = device.device_id
        table_row_id_device_map[table_row_id] = device_id
        # update_notify user map
        DEFAULT_BATTERY_LEVEL_TO_NOTIFY = 80
        device_battery_level_to_notify_map[device_id] = BatteryLevelToNotify(DEFAULT_BATTERY_LEVEL_TO_NOTIFY)


def _get_device_battery_level_from_table(devices_list: QTableWidget, row: int) -> str:
    return devices_list.item(row, _DeviceTableRecord.BATTERY_LEVEL_COLUMN.value)


def _update_device_battery_level_in_table(devices_list: QTableWidget, row: int, value: str) -> None:
    devices_list.item(row, _DeviceTableRecord.BATTERY_LEVEL_COLUMN.value).setText(value)


def _insert_new_registered_device_to_table(devices_list: QTableWidget, new_device: Device) -> int:
    row_position = devices_list.rowCount()
    devices_list.insertRow(row_position)

    device_name_table_item = QTableWidgetItem(new_device.device_name)
    devices_list.setItem(row_position, _DeviceTableRecord.DEVICE_NAME_COLUMN.value, device_name_table_item)
    _set_cell_as_immutable(devices_list.item(row_position, _DeviceTableRecord.DEVICE_NAME_COLUMN.value))

    battery_level_table_item = QTableWidgetItem(new_device.battery_level)
    devices_list.setItem(row_position, _DeviceTableRecord.BATTERY_LEVEL_COLUMN.value, battery_level_table_item)
    _set_cell_as_immutable(devices_list.item(row_position, _DeviceTableRecord.BATTERY_LEVEL_COLUMN.value))

    notify_battery_level_table_item = QTableWidgetItem(_DeviceTableRecord.DEFAULT_BATTERY_LEVEL_TO_NOTIFY.value)
    devices_list.setItem(row_position, _DeviceTableRecord.BATTERY_LEVEL_COLUMN.value, notify_battery_level_table_item)
    _set_cell_as_immutable(devices_list.item(row_position, _DeviceTableRecord.BATTERY_LEVEL_TO_NOTIFY_COLUMN.value))

    return row_position


def _remove_new_registered_device_from_table(devices_list: QTableWidget, device_row_id: int):
    devices_list.removeRow(device_row_id)
    # remove from map and notify


def notify_user_if_device_battery_level_hits_quota(device_list: QTableWidget,
                                                   device_battery_level_to_notify_map: Dict[str, BatteryLevelToNotify],
                                                   table_row_id_device_map: Dict[int, str]):
    row_count = device_list.rowCount()

    for row_index in range(row_count):
        device_id: str = table_row_id_device_map[row_index]

        device_battery_notification: BatteryLevelToNotify = device_battery_level_to_notify_map[device_id]
        device_current_battery_level: int = int(
            device_list.item(row_index, _DeviceTableRecord.BATTERY_LEVEL_COLUMN.value).text())

        if device_current_battery_level < device_battery_notification.battery_level_to_notify \
                or device_battery_notification.has_notified:
            continue

        # notify user
        print(f'notified user!')
        device_battery_notification.has_notified = True
        device_battery_level_to_notify_map[device_id] = device_battery_notification
