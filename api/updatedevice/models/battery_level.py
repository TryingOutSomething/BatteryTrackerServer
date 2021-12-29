from pydantic import BaseModel


class DeviceBatteryInfo(BaseModel):
    device_id: str
    current_battery_level: str
