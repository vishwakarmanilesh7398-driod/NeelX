from android.device import AndroidDevice
from android.screenshot import Screenshot

device = AndroidDevice()

try:

    device.connect()

    image = Screenshot.capture()

    print("✅ Screenshot Saved")

    print(image)

except Exception as e:

    print(e)