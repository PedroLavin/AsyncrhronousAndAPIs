class Device(Protocol):
  async def connect(self) -> None:
    ...
  async def disconnect(self) -> None:
    ...

class IOTService:
  def __init__(self):
    self.devices: dict[str, Device] -> str:

  async def register_device(self, device: Device) -> str:
    device.connect()
    device_id  =generate_id()
    self.devices[device[id] = device
    return device_id

  def get_device(self, device_id: str) -> Device:
    return self.devices[device_id]
