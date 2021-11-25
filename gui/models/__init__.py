from enum import Enum
from typing import Callable, Dict


class BatteryLevelToNotify:
    def __init__(self, battery_level: int):
        self.battery_level_to_notify: int = battery_level
        self.has_notified: bool = False


class TableWidgetCallbackIdentifiers(Enum):
    UPDATE_BATTERY_NOTIFICATION_ENTRY = 0
    REMOVE_MAP_ENTRIES_ASSOCIATED_TO_TABLE_ROW_ID = 1
    MAP_TABLE_ROW_ID_TO_DEVICE = 2


class TableWidgetCallbacks:
    def __init__(self):
        self._callbacks: Dict[TableWidgetCallbackIdentifiers, Callable] = {}

    def register_callback(self, key: TableWidgetCallbackIdentifiers, callback: Callable) -> None:
        self._callbacks[key] = callback

    def get_callback(self, key: TableWidgetCallbackIdentifiers) -> Callable:
        if key not in self._callbacks:
            raise KeyError('Callback not registered!')

        return self._callbacks[key]


class SyncTableWithRegistryParams:
    def __init__(self,
                 devices_registry: dict,
                 table_id_device_map: dict,
                 callbacks: TableWidgetCallbacks):
        self.devices_registry: dict = devices_registry
        self.table_id_device_map: dict = table_id_device_map
        self.callbacks: TableWidgetCallbacks = callbacks
