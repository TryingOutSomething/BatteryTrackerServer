import sys
from typing import Dict

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow

from gui.app_template import Ui_MainWindow
from gui.gui_callback_actions import (change_interval_actions,
                                      table_widget_actions as table_actions)
from gui.gui_callback_actions.table_widget_actions import BatteryLevelToNotify
from shared_cache import get_all_registered_devices


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Interface, self).__init__(parent)

        self._retrieve_device_info_interval: int = 0
        self._is_modifying_input: bool = False
        self._device_battery_level_to_notify_map: Dict[str, BatteryLevelToNotify] = {}
        self._table_row_id_device_map: Dict[int, str] = {}
        self._timer: QTimer = QTimer(self)

        self.setupUi(self)
        self.post_ui_setup_initialisation()

    def post_ui_setup_initialisation(self):
        self.changeIntervalButton.clicked.connect(self._change_retrieval_interval)
        self._retrieve_device_info_interval = change_interval_actions.get_current_retrieval_interval(self.intervalInput)

        self.intervalInput.textChanged.connect(self._on_text_input_changed)
        self.devicesList.cellChanged.connect(self._on_notify_percentage_changed)

        table_actions.set_allow_only_last_column_editable(self.devicesList)

        self._timer.timeout.connect(self._sync_shared_cache_with_gui)
        self.startIntervalButton.clicked.connect(self._start_repeating_event)
        self.stopIntervalButton.clicked.connect(self._stop_repeating_event)

    def _start_repeating_event(self):
        self._timer.start(_seconds_to_milliseconds(self._retrieve_device_info_interval))
        self.startIntervalButton.setEnabled(False)
        self.stopIntervalButton.setEnabled(True)

    def _stop_repeating_event(self):
        self._timer.stop()
        self.stopIntervalButton.setEnabled(False)
        self.startIntervalButton.setEnabled(True)

    def _change_retrieval_interval(self):
        new_interval: int = change_interval_actions.get_current_retrieval_interval(self.intervalInput)

        if _is_invalid_retrieval_interval(self._retrieve_device_info_interval, new_interval):
            self._display_error_message('same or invalid value')
            return

        self._retrieve_device_info_interval = new_interval
        self._start_repeating_event()

        change_interval_actions.reset_input_container_styles(self.refreshIntervalLabel,
                                                             self._should_show_modifying_input_styles)

    def _on_text_input_changed(self):
        if self._is_modifying_input:
            return

        change_interval_actions.show_modified_input_container_styles(self.refreshIntervalLabel,
                                                                     self._should_show_modifying_input_styles)

    def _should_show_modifying_input_styles(self, is_modifying_input: bool) -> None:
        self._is_modifying_input = is_modifying_input
        self.changeIntervalButton.setEnabled(is_modifying_input)

    def _display_error_message(self, error_message: str):
        self.errorLabel.setText(error_message)

    def _on_notify_percentage_changed(self, row, column):
        if len(self._table_row_id_device_map) <= 0:
            return

        updated_battery_notify_level = self.devicesList.item(row, column)

        if not change_interval_actions.is_invalid_input_text(updated_battery_notify_level):
            self._display_error_message('Invalid battery level!')
            return

        device_id = self._table_row_id_device_map[row]
        self._device_battery_level_to_notify_map[device_id] = BatteryLevelToNotify(int(updated_battery_notify_level))

    def _sync_shared_cache_with_gui(self):
        print('syncing')
        table_actions.sync_shared_cache_with_gui(self.devicesList,
                                                 get_all_registered_devices(),
                                                 self._table_row_id_device_map,
                                                 self._device_battery_level_to_notify_map)

        table_actions.notify_user_if_device_battery_level_hits_quota(self.devicesList,
                                                                     self._device_battery_level_to_notify_map,
                                                                     self._table_row_id_device_map)


def _is_invalid_retrieval_interval(current_interval: int, new_interval: int) -> bool:
    return new_interval < 0 or new_interval == current_interval


def _seconds_to_milliseconds(seconds: int) -> int:
    return seconds * 1000


def start_gui():
    app = QApplication()
    interface = Interface()
    interface.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_gui()
