from pydantic import BaseModel


class Device(BaseModel):
    device_id: str
    device_name: str
    battery_level: str

    def __hash__(self):
        return id(self)

    def __eq__(self, other: 'Device'):
        return self.device_id == other.device_id and \
               self.device_name == other.device_name and \
               self.battery_level == other.battery_level


class UnregisterDevice(BaseModel):
    device_id: str
