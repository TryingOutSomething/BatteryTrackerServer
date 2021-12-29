from typing import Callable

from PySide6.QtWidgets import QLineEdit, QLabel

_FONT_WEIGHT_BOLD_STYLE = 'font-weight:bold'
_FONT_WEIGHT_NORMAL_STYLE = 'font-weight:normal'


def get_current_retrieval_interval(text_input: QLineEdit, is_invalid_input: Callable[[str], bool]) -> int:
    text: str = _get_input_text(text_input)

    if is_invalid_input(text):
        return -1

    return int(text)


def _get_input_text(text_input: QLineEdit) -> str:
    return text_input.text()


def apply_modified_input_styles(label: QLabel,
                                on_editing_input: Callable[[bool], None]) -> None:
    on_editing_input(True)
    _apply_modified_input_label_styles(label)


def _apply_modified_input_label_styles(change_interval_label: QLabel) -> None:
    label_text = change_interval_label.text()
    label_text += '*'
    change_interval_label.setText(label_text)
    change_interval_label.setStyleSheet(_FONT_WEIGHT_BOLD_STYLE)


def reset_modified_input_styles(change_interval_label: QLabel,
                                on_submit_input_changes: Callable[[bool], None]) -> None:
    on_submit_input_changes(False)
    _clear_modified_input_label_styles(change_interval_label)


def _clear_modified_input_label_styles(change_interval_label: QLabel) -> None:
    label_text = change_interval_label.text()
    label_text = label_text[:-1]
    change_interval_label.setText(label_text)
    change_interval_label.setStyleSheet(_FONT_WEIGHT_NORMAL_STYLE)
