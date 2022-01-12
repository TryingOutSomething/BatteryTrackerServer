from os.path import abspath, dirname, join

_CURRENT_DIRECTORY_PATH = dirname(abspath(__file__))
_BASE_ASSET_PATH = join(_CURRENT_DIRECTORY_PATH, 'images')
_WINDOW_ICON = 'favicon.png'
_TOAST_ICON = 'toasticon.ico'


def get_window_icon_path():
    return join(_BASE_ASSET_PATH, _WINDOW_ICON)


def get_toast_icon_path():
    return join(_BASE_ASSET_PATH, _TOAST_ICON)
