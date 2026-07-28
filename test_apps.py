"""
=========================================
Project : NeelX
Module  : Apps Test
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import time

from android.device import AndroidDevice
from core.apps.manager import Apps


def main():

    if not AndroidDevice.is_connected():
        print("❌ Device Not Connected")
        return

    print("✅ Device Connected")

    print("Opening Settings...")
    Apps.open("settings")

    time.sleep(5)

    print("Closing Settings...")
    Apps.close("settings")

    print("✅ Test Completed")


if __name__ == "__main__":
    main()