"""
=========================================
Project : NeelX
Module  : Android API Test
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import time

from android.api import Android


def main():

    if not Android.is_connected():
        print("❌ Device Not Connected")
        return

    print("✅ Connected")

    print("Brand :", Android.brand())
    print("Model :", Android.model())
    print("Android :", Android.android_version())
    print("Resolution :", Android.resolution())

    print("\nOpening Settings...")
    Android.open("com.android.settings")

    time.sleep(3)

    print("Going Home...")
    Android.home()

    print("Taking Screenshot...")
    path = Android.screenshot()

    print("Saved :", path)

    print("Done ✅")


if __name__ == "__main__":
    main()