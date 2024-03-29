import sys
from datetime import datetime
from typing import Dict

import qdarktheme
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from database.shared_cache import get_all_registered_devices
from gui.actions.devicetable import table_actions
from gui.actions.models import (BatteryLevelToNotify,
                                TableWidgetCallbacks,
                                TableWidgetCallbackIdentifiers,
                                SyncTableWithRegistryParams, BatteryNotificationParams)
from gui.actions.retrievedevices import input_actions
from gui.actions.status import status_actions
from gui.app_template import Ui_MainWindow
from gui.assets import get_window_icon_path


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self, server_address, parent=None):
        super(Interface, self).__init__(parent)

        self._retrieve_device_info_interval: int = 0
        self._is_modifying_input: bool = False
        self._device_battery_level_to_notify_map: Dict[str, BatteryLevelToNotify] = {}
        self._table_row_id_device_map: Dict[int, str] = {}
        self._server_address = server_address

        self._timer: QTimer = QTimer(self)
        self._table_widget_callbacks: TableWidgetCallbacks = self.register_table_widget_callbacks()

        self.setupUi(self)
        self._post_ui_setup_initialisation()

    def _post_ui_setup_initialisation(self):
        self.setWindowTitle(f'Battery Information | {self._server_address}')
        self._apply_global_styles()

        self._setup_change_interval_container_actions()
        self._setup_start_stop_refresh_interval_actions()
        self._setup_device_table_actions()

    def _apply_global_styles(self):
        window_icon: QIcon = QIcon(get_window_icon_path())
        self.setWindowIcon(window_icon)
        self.setStyleSheet(qdarktheme.load_stylesheet())

    def _setup_change_interval_container_actions(self):
        self.changeIntervalButton.clicked.connect(self._change_retrieval_interval)
        self._retrieve_device_info_interval = input_actions.get_current_retrieval_interval(self.intervalInput,
                                                                                           _is_invalid_input_text)

    def _change_retrieval_interval(self):
        new_interval: int = input_actions.get_current_retrieval_interval(self.intervalInput, _is_invalid_input_text)

        if _is_invalid_retrieval_interval(self._retrieve_device_info_interval, new_interval):
            self._display_error_message('Same or invalid value')
            return

        self._retrieve_device_info_interval = new_interval
        input_actions.reset_modified_input_styles(self.refreshIntervalLabel,
                                                  self._should_show_modifying_input_styles)
        self._display_error_message('')

    def _setup_start_stop_refresh_interval_actions(self):
        self._timer.timeout.connect(self._sync_shared_cache_with_gui)
        self.startIntervalButton.clicked.connect(self._start_repeating_event)
        self.stopIntervalButton.clicked.connect(self._stop_repeating_event)

    def _sync_shared_cache_with_gui(self):
        status_actions.set_updating_status(self.statusLabel)
        print(f'GUI: \t{_get_current_timestamp()} - SYNCING DATABASE...')

        sync_table_args = SyncTableWithRegistryParams(get_all_registered_devices(),
                                                      self._table_row_id_device_map,
                                                      self._table_widget_callbacks)

        table_actions.sync_shared_cache_with_gui(self.devicesList, sync_table_args)

        notify_device_args = BatteryNotificationParams(self._device_battery_level_to_notify_map,
                                                       self._table_row_id_device_map,
                                                       self._on_update_battery_notification_status,
                                                       self.window().windowTitle())

        table_actions.notify_device_battery_level_hits_threshold(self.devicesList,
                                                                 notify_device_args)
        status_actions.set_start_status(self.statusLabel)

    def _start_repeating_event(self):
        status_actions.set_start_status(self.statusLabel)
        self._timer.start(_seconds_to_milliseconds(self._retrieve_device_info_interval))

        self.startIntervalButton.setEnabled(False)
        self.stopIntervalButton.setEnabled(True)

        self._sync_shared_cache_with_gui()

    def _stop_repeating_event(self):
        self._timer.stop()
        status_actions.set_idle_status(self.statusLabel)

        self.stopIntervalButton.setEnabled(False)
        self.startIntervalButton.setEnabled(True)

    def _setup_device_table_actions(self):
        self.intervalInput.textChanged.connect(self._on_text_input_changed)
        self.devicesList.cellChanged.connect(self._on_notify_percentage_changed)

    def _on_text_input_changed(self):
        if self._is_modifying_input:
            return

        input_actions.apply_modified_input_styles(self.refreshIntervalLabel,
                                                  self._should_show_modifying_input_styles)

    def _should_show_modifying_input_styles(self, is_modifying_input: bool) -> None:
        self._is_modifying_input = is_modifying_input
        self.changeIntervalButton.setEnabled(is_modifying_input)

    def _display_error_message(self, error_message: str):
        self.errorLabel.setText(error_message)

    def _on_notify_percentage_changed(self, row, column):
        if (len(self._table_row_id_device_map) <= 0 or
                column != table_actions.BATTERY_LEVEL_TO_NOTIFY_COLUMN or
                row not in self._table_row_id_device_map):
            # Newly inserted row or empty table
            return

        device_id = self._table_row_id_device_map[row]
        battery_level_to_notify = self.devicesList.item(row, column).text()

        if _is_invalid_input_text(battery_level_to_notify):
            self._display_error_message('Invalid battery level!')
            return

        updated_battery_notification = BatteryLevelToNotify(int(battery_level_to_notify))
        self._on_update_battery_notification_status(device_id, updated_battery_notification)
        self._display_error_message('')

    def _on_insert_new_device_to_table(self, row_id: int, device_id: str, battery_notification: BatteryLevelToNotify):
        self._table_row_id_device_map[row_id] = device_id
        self._on_update_battery_notification_status(device_id, battery_notification)

    def _on_update_battery_notification_status(self, device_id: str, battery_notification: BatteryLevelToNotify):
        self._device_battery_level_to_notify_map[device_id] = battery_notification

    def _on_remove_device_from_table(self, row_id: int) -> None:
        device_id = self._table_row_id_device_map[row_id]

        self._table_row_id_device_map.pop(row_id)
        self._device_battery_level_to_notify_map.pop(device_id)

    def register_table_widget_callbacks(self) -> TableWidgetCallbacks:
        callback_registry = TableWidgetCallbacks()

        callback_registry.register_callback(
            TableWidgetCallbackIdentifiers.REMOVE_MAP_ENTRIES_ASSOCIATED_TO_TABLE_ROW_ID,
            self._on_remove_device_from_table)

        callback_registry.register_callback(
            TableWidgetCallbackIdentifiers.MAP_TABLE_ROW_ID_TO_DEVICE,
            self._on_insert_new_device_to_table)

        return callback_registry


def _is_invalid_retrieval_interval(current_interval: int, new_interval: int) -> bool:
    return new_interval < 0 or new_interval == current_interval


def _is_invalid_input_text(text: str) -> bool:
    return not text or not text.isdigit()


def _seconds_to_milliseconds(seconds: int) -> int:
    return seconds * 1000


def _get_current_timestamp() -> str:
    now = datetime.now()

    return datetime.strftime(now, '%d/%m/%Y %H:%M:%S:%f')


def start_gui(server_address):
    app = QApplication()
    interface = Interface(server_address)
    interface.show()
    sys.exit(app.exec())
