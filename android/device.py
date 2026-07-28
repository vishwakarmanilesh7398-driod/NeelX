"""
=========================================
Project : NeelX
Module  : Android Device
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from android.adb import ADB
from android.exceptions import DeviceNotFoundError


class AndroidDevice:

    def __init__(self):
        self.connected = False

    def connect(self) -> bool:
        """
        Check if an Android device is connected.
        """

        output = ADB.devices()

        lines = output.splitlines()

        devices = []

        for line in lines[1:]:

            line = line.strip()

            if line and "\tdevice" in line:
                devices.append(line)

        if not devices:
            raise DeviceNotFoundError(
                "No Android device connected."
            )

        self.connected = True

        return True

    def model(self) -> str:

        return ADB.shell(
            "getprop ro.product.model"
        )

    def brand(self) -> str:

        return ADB.shell(
            "getprop ro.product.brand"
        )

    def android_version(self) -> str:

        return ADB.shell(
            "getprop ro.build.version.release"
        )

    def battery(self) -> str:

        return ADB.shell(
            "dumpsys battery"
        )

    def screen_size(self) -> str:

        return ADB.shell(
            "wm size"
        )