from plyer import notification

from gui.assets import get_toast_icon_path

_TITLE: str = 'Device Battery Notifier'
_NOTIFICATION_DISPLAY_DURATION: int = 20
_APP_ICON_PATH: str = get_toast_icon_path()
_DEFAULT_APP_NAME = 'Battery Information'


def notify_device_charged(payload: str, app_name='') -> None:
    notification.notify(title=_TITLE,
                        message=payload,
                        app_icon=_APP_ICON_PATH,
                        app_name=app_name if app_name else _DEFAULT_APP_NAME,
                        timeout=_NOTIFICATION_DISPLAY_DURATION)
