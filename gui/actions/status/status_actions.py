from PySide6.QtWidgets import QLabel

_IDLE_STATUS_TEXT = 'IDLE'
_IDLE_LABEL_COLOUR = '#e91e63'

_START_STATUS_TEXT = 'RETRIEVING'
_START_LABEL_COLOUR = '#4caf50'

_UPDATING_STATUS_TEXT = 'UPDATING'
_UPDATING_LABEL_COLOUR = '#2196f3'


def set_start_status(label: QLabel):
    _change_status_text(label, _START_STATUS_TEXT)
    _set_label_colour(label, _START_LABEL_COLOUR)


def set_idle_status(label: QLabel):
    _change_status_text(label, _IDLE_STATUS_TEXT)
    _set_label_colour(label, _IDLE_LABEL_COLOUR)


def set_updating_status(label: QLabel):
    _change_status_text(label, _UPDATING_STATUS_TEXT)
    _set_label_colour(label, _UPDATING_LABEL_COLOUR)


def _change_status_text(label: QLabel, status: str):
    label.setText(status)


def _set_label_colour(label: QLabel, colour: str):
    label.setStyleSheet(f'color: {colour}')
