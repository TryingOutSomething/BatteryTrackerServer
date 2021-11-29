from plyer import notification

_TITLE: str = 'Device Battery Notifier'
_NOTIFICATION_DISPLAY_DURATION: int = 5
_APP_ICON_PATH: str = ''


def notify_device_charged(payload: str) -> None:
    notification.notify(title=_TITLE,
                        message=payload,
                        app_icon=_APP_ICON_PATH,
                        timeout=_NOTIFICATION_DISPLAY_DURATION)
