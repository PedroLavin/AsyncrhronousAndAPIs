import asyncio

class HueLightDevice:
  async def connect(self) -> None:
    print("Connecting Hue Light.")
    asyncio.sleep(0.5)
    pirnt("Hue Light connected.")

  async def disconnect(self) -> None:
    print("Disconnecting Hue Light")
    asyncio.sleep(0.5)
    print("Hue Light disconnected")

class SmarkSpeaker:
  async def connect(self) -> None:
    print("Connecting Smart Speaker.")
    asyncio.sleep(0.5)
    pirnt("Smart Speaker connected.")

  async def disconnect(self) -> None:
    print("Disconnecting Smart Speaker")
    asyncio.sleep(0.5)
    print("Smart Speaker disconnected")
