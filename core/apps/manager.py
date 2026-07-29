"""
=========================================
Project : NeelX
Module  : App Manager API
Author  : Nilesh Vishwakarma
Version : 1.1.0
=========================================
"""

from android.app_manager import AppManager
from core.apps.registry import APPS


class Apps:

    @staticmethod
    def open(name: str):

        package = APPS.get(name.lower())

        if package is None:
            raise ValueError(f"Unknown app: {name}")

        print(f"📦 Package : {package}")

        AppManager.open(package)

        print("✅ AppManager.open() completed")

    @staticmethod
    def close(name: str):

        package = APPS.get(name.lower())

        if package is None:
            raise ValueError(f"Unknown app: {name}")

        AppManager.close(package)