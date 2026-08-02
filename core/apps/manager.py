"""
=========================================
Project : NeelX
Module  : App Manager API
Author  : Nilesh Vishwakarma
Version : 1.2.0
=========================================
"""

from android.app_manager import AppManager
from core.apps.registry import APPS
from core.nlp.fuzzy import Fuzzy


class Apps:

    @staticmethod
    def open(name: str):

        name = name.lower().strip()

        package = APPS.get(name)

        # Fuzzy Match
        if package is None:

            match = Fuzzy.match(
                name,
                list(APPS.keys())
            )

            if match:
                print(f"🧠 Fuzzy Match : {name} -> {match}")
                package = APPS[match]
                name = match

        if package is None:
            raise ValueError(f"Unknown app: {name}")

        print(f"📱 Opening : {name}")
        print(f"📦 Package : {package}")

        AppManager.open(package)

        print("✅ AppManager.open() completed")

    @staticmethod
    def close(name: str):

        name = name.lower().strip()

        package = APPS.get(name)

        if package is None:

            match = Fuzzy.match(
                name,
                list(APPS.keys())
            )

            if match:
                print(f"🧠 Fuzzy Match : {name} -> {match}")
                package = APPS[match]
                name = match

        if package is None:
            raise ValueError(f"Unknown app: {name}")

        AppManager.close(package)