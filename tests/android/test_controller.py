from android.device import AndroidDevice
from android.controller import AndroidController

device = AndroidDevice()

try:

    device.connect()

    print("✅ Connected:", device.model())

    print("Going Home...")

    AndroidController.home()

except Exception as e:

    print(e)