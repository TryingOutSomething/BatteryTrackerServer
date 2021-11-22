from typing import Callable

from PySide6.QtWidgets import QLineEdit, QLabel

_FONT_WEIGHT_BOLD_STYLE = 'font-weight:bold'
_FONT_WEIGHT_NORMAL_STYLE = 'font-weight:normal'


def get_current_retrieval_interval(text_input: QLineEdit) -> int:
    text: str = get_input_text(text_input)

    if is_invalid_input_text(text):
        return -1

    return int(text)


def get_input_text(text_input: QLineEdit) -> str:
    return text_input.text()


def is_invalid_input_text(text: str) -> bool:
    return not text or not text.isdigit()


def show_modified_input_container_styles(change_interval_label: QLabel,
                                         on_editing_input: Callable[[bool], None]) -> None:
    on_editing_input(True)
    _set_modified_input_label_styles(change_interval_label)


def _set_modified_input_label_styles(change_interval_label: QLabel) -> None:
    label_text = change_interval_label.text()
    label_text += '*'
    change_interval_label.setText(label_text)
    change_interval_label.setStyleSheet(_FONT_WEIGHT_BOLD_STYLE)


def reset_input_container_styles(change_interval_label: QLabel,
                                 on_submit_input_changes: Callable[[bool], None]) -> None:
    on_submit_input_changes(False)
    _clear_modified_input_label_styles(change_interval_label)


def _clear_modified_input_label_styles(change_interval_label: QLabel) -> None:
    label_text = change_interval_label.text()
    label_text = label_text[:-1]
    change_interval_label.setText(label_text)
    change_interval_label.setStyleSheet(_FONT_WEIGHT_NORMAL_STYLE)
