from os.path import abspath, join

_BASE_ASSET_PATH = abspath('./gui/assets/images/')
_WINDOW_ICON = 'favicon.png'
_TOAST_ICON = 'toasticon.ico'


def get_window_icon_path():
    return join(_BASE_ASSET_PATH, _WINDOW_ICON)


def get_toast_icon_path():
    return join(_BASE_ASSET_PATH, _TOAST_ICON)
