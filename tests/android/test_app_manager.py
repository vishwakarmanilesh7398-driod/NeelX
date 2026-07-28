from android.device import AndroidDevice
from android.app_manager import AppManager
import time

device = AndroidDevice()

device.connect()

print("✅ Connected :", device.model())

PACKAGE = "com.android.settings"

print("📦 Installed :", AppManager.is_installed(PACKAGE))

print("🚀 Opening Settings...")
AppManager.open(PACKAGE)

time.sleep(5)

print("❌ Closing Settings...")
AppManager.close(PACKAGE)

print("✅ Test Completed.")