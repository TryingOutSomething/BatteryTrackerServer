from typing import Dict, List, Callable, Tuple

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from gui.models import SyncTableWithRegistryParams, TableWidgetCallbackIdentifiers, BatteryLevelToNotify
from register_devices.models.device import Device

DEVICE_NAME_COLUMN = 0
BATTERY_LEVEL_COLUMN = 1
BATTERY_LEVEL_TO_NOTIFY_COLUMN = 2
_DEFAULT_BATTERY_LEVEL_TO_NOTIFY = 80

_FilteredDevicesInfo = Tuple[Dict[str, Device], List[int], List[int]]


def set_allow_only_last_column_editable(devices_list: QTableWidget) -> None:
    for row in range(devices_list.rowCount()):
        for col in range(devices_list.columnCount() - 1):
            _set_cell_as_immutable(devices_list.item(row, col))


def _set_cell_as_immutable(cell: QTableWidgetItem):
    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)


def sync_shared_cache_with_gui(devices_table: QTableWidget,
                               sync_table_with_registry_params: SyncTableWithRegistryParams):
    (registered_devices_dict,
     updating_devices_info,
     evicting_devices_row_id) = _identify_evicting_and_registered_devices(devices_table,
                                                                          sync_table_with_registry_params)

    remove_related_entries: Callable[[int], None] = sync_table_with_registry_params.callbacks.get_callback(
        TableWidgetCallbackIdentifiers.REMOVE_MAP_ENTRIES_ASSOCIATED_TO_TABLE_ROW_ID)

    _remove_devices_from_table_and_related_maps(devices_table, evicting_devices_row_id, remove_related_entries)
    _update_devices_from_table_and_related_maps(devices_table, updating_devices_info, sync_table_with_registry_params)
    _insert_new_devices_to_table_and_related_maps(devices_table, registered_devices_dict,
                                                  sync_table_with_registry_params)


def _identify_evicting_and_registered_devices(devices_table: QTableWidget,
                                              sync_table_with_registry_params: SyncTableWithRegistryParams) -> _FilteredDevicesInfo:
    registered_devices_dict: Dict[str, Device] = {}
    updating_devices_info: List[int] = []
    evicting_devices_row_id: List[int] = []

    no_of_devices_in_table: int = devices_table.rowCount()

    device_registry = sync_table_with_registry_params.devices_registry
    table_id_device_map = sync_table_with_registry_params.table_id_device_map

    if no_of_devices_in_table <= 0:
        return registered_devices_dict, updating_devices_info, evicting_devices_row_id

    for i in range(no_of_devices_in_table):
        device_id: str = table_id_device_map[i]

        if device_id not in device_registry:
            evicting_devices_row_id.append(i)
            continue

        registered_devices_dict[device_id] = device_registry[device_id]

        device_in_registry: Device = device_registry[device_id]
        device_battery_level = _get_device_battery_level_from_table(devices_table, i)

        if device_battery_level == device_in_registry.battery_level:
            continue

        updating_devices_info.append(i)

    return registered_devices_dict, updating_devices_info, evicting_devices_row_id


def _remove_devices_from_table_and_related_maps(devices_table: QTableWidget,
                                                evicting_devices_row_id: List[int],
                                                remove_related_entries: Callable) -> None:
    for row_id in evicting_devices_row_id:
        _remove_device_from_table(devices_table, row_id)
        remove_related_entries(row_id)


def _update_devices_from_table_and_related_maps(devices_table: QTableWidget,
                                                updating_devices_info: List[int],
                                                sync_table_with_registry_params: SyncTableWithRegistryParams):
    devices_registry = sync_table_with_registry_params.devices_registry
    table_id_device_map = sync_table_with_registry_params.table_id_device_map

    for row_id in updating_devices_info:
        device_id: str = table_id_device_map[row_id]
        device_in_registry: Device = devices_registry[device_id]
        updated_battery_level: str = device_in_registry.battery_level

        _update_device_battery_in_table(devices_table, row_id, updated_battery_level)


def _insert_new_devices_to_table_and_related_maps(devices_table: QTableWidget,
                                                  registered_devices_dict: Dict[str, Device],
                                                  sync_table_with_registry_params: SyncTableWithRegistryParams):
    devices_registry: Dict[str, Device] = sync_table_with_registry_params.devices_registry
    new_devices: Dict[str, Device] = _identify_new_devices(registered_devices_dict, devices_registry)

    insert_related_entries: Callable[[int, str, BatteryLevelToNotify],
                                     None] = sync_table_with_registry_params.callbacks.get_callback(
        TableWidgetCallbackIdentifiers.MAP_TABLE_ROW_ID_TO_DEVICE
    )

    for device_id, device in new_devices.items():
        inserted_row_id: int = _insert_device_to_table(devices_table, device)
        new_battery_notification = BatteryLevelToNotify(_DEFAULT_BATTERY_LEVEL_TO_NOTIFY)

        insert_related_entries(inserted_row_id, device_id, new_battery_notification)


def _identify_new_devices(registered_devices_dict: Dict[str, Device], devices_registry: Dict[str, Device]) -> dict:
    registered_devices_set: set = set(registered_devices_dict.items())
    devices_registry_set: set = set(devices_registry.items())

    new_devices_set: set = devices_registry_set - registered_devices_set

    return dict(new_devices_set)


def _get_device_battery_level_from_table(devices_table: QTableWidget, row: int) -> str:
    return _get_item_from_table(devices_table, row, BATTERY_LEVEL_COLUMN)


def _get_item_from_table(devices_table: QTableWidget, row: int, column: int) -> str:
    return devices_table.item(row, column).text()


def _remove_device_from_table(devices_table: QTableWidget, row: int) -> None:
    devices_table.removeRow(row)


def _update_device_battery_in_table(devices_table, row: int, item: str):
    new_item = QTableWidgetItem(item)

    _update_device_in_table(devices_table, row, BATTERY_LEVEL_COLUMN, new_item)


def _update_device_in_table(devices_table: QTableWidget, row: int, column: int, item: QTableWidgetItem):
    devices_table.setItem(row, column, item)


def _insert_device_to_table(devices_table: QTableWidget, device: Device) -> int:
    row_position = devices_table.rowCount()
    devices_table.insertRow(row_position)

    device_name_item = QTableWidgetItem(device.device_name)
    battery_level = QTableWidgetItem(device.battery_level)
    battery_level_to_notify = QTableWidgetItem(str(_DEFAULT_BATTERY_LEVEL_TO_NOTIFY))

    _update_device_in_table(devices_table, row_position, DEVICE_NAME_COLUMN, device_name_item)
    _update_device_in_table(devices_table, row_position, BATTERY_LEVEL_COLUMN, battery_level)
    _update_device_in_table(devices_table, row_position, BATTERY_LEVEL_TO_NOTIFY_COLUMN, battery_level_to_notify)

    return row_position


def notify_device_battery_level_hits_threshold(devices_table: QTableWidget,
                                               device_battery_level_to_notify_map: Dict[str, BatteryLevelToNotify],
                                               table_row_id_device_map: Dict[int, str],
                                               on_update_battery_notification_status: Callable[
                                                   [str, BatteryLevelToNotify], None]):
    row_count: int = devices_table.rowCount()

    if row_count <= 0:
        return

    for i in range(row_count):
        device_id: str = table_row_id_device_map[i]
        device_battery_notification: BatteryLevelToNotify = device_battery_level_to_notify_map[device_id]

        device_battery_level_in_table: int = int(_get_device_battery_level_from_table(devices_table, i))

        if (device_battery_level_in_table < device_battery_notification.battery_level_to_notify or
                device_battery_notification.has_notified):
            continue

        print(f'Notified about device {device_id}, row {i}')
        device_battery_notification.has_notified = True
        on_update_battery_notification_status(device_id, device_battery_notification)
