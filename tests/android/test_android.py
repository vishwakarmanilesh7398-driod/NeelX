from android.device import AndroidDevice

device = AndroidDevice()

try:

    device.connect()

    print("✅ Device Connected")

    print("Model :", device.model())
    print("Brand :", device.brand())
    print("Android :", device.android_version())
    print("Resolution :", device.screen_size())

except Exception as e:

    print("❌", e)