"""
=========================================
Project : NeelX
Module  : App Manager
Author  : Nilesh Vishwakarma
Version : 1.1.0
=========================================
"""

from android.adb import ADB


class AppManager:

    @staticmethod
    def open(package_name: str):

        ADB.shell(
            f"am start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -p {package_name}"
        )

    @staticmethod
    def close(package_name: str):

        ADB.shell(
            f"am force-stop {package_name}"
        )

    @staticmethod
    def is_installed(package_name: str) -> bool:

        result = ADB.shell(
            f"pm list packages {package_name}"
        )

        return package_name in result

    @staticmethod
    def list_packages():

        result = ADB.shell(
            "pm list packages"
        )

        return result.splitlines()