"""
=========================================
Project : NeelX
Module  : Android Device
Author  : Nilesh Vishwakarma
Version : 2.0.0
=========================================
"""

import subprocess

from android.adb import ADB


class AndroidDevice:

    @staticmethod
    def is_connected() -> bool:
        """
        Check whether at least one Android device is connected.
        """
        result = subprocess.run(
            [str(ADB.ADB_PATH), "devices"],
            capture_output=True,
            text=True
        )

        lines = result.stdout.strip().splitlines()

        for line in lines[1:]:
            if "\tdevice" in line:
                return True

        return False

    @staticmethod
    def connect():

        if not AndroidDevice.is_connected():
            raise RuntimeError("No Android device connected.")

        return True

    @staticmethod
    def shell(command: str):

        result = subprocess.run(
            [
                str(ADB.ADB_PATH),
                "shell",
                command
            ],
            capture_output=True,
            text=True
        )

        return result.stdout.strip()

    @staticmethod
    def model():

        return AndroidDevice.shell(
            "getprop ro.product.model"
        )

    @staticmethod
    def brand():

        return AndroidDevice.shell(
            "getprop ro.product.brand"
        )

    @staticmethod
    def android_version():

        return AndroidDevice.shell(
            "getprop ro.build.version.release"
        )

    @staticmethod
    def resolution():

        return AndroidDevice.shell(
            "wm size"
        )