"""
=========================================
Project : NeelX
Module  : Android API
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from pathlib import Path

from android.device import AndroidDevice
from android.controller import AndroidController
from android.screenshot import Screenshot
from android.app_manager import AppManager
from android.recorder import Recorder


class Android:

    # -------------------------
    # Device
    # -------------------------

    @staticmethod
    def connect() -> bool:
        return AndroidDevice.connect()

    @staticmethod
    def is_connected() -> bool:
        return AndroidDevice.is_connected()

    @staticmethod
    def model() -> str:
        return AndroidDevice.model()

    @staticmethod
    def brand() -> str:
        return AndroidDevice.brand()

    @staticmethod
    def android_version() -> str:
        return AndroidDevice.android_version()

    @staticmethod
    def resolution() -> str:
        return AndroidDevice.resolution()

    # -------------------------
    # Controller
    # -------------------------

    @staticmethod
    def tap(x: int, y: int):
        AndroidController.tap(x, y)

    @staticmethod
    def swipe(x1, y1, x2, y2, duration=300):
        AndroidController.swipe(x1, y1, x2, y2, duration)

    @staticmethod
    def home():
        AndroidController.home()

    @staticmethod
    def back():
        AndroidController.back()

    @staticmethod
    def recent():
        AndroidController.recent()

    # -------------------------
    # Screenshot
    # -------------------------

    @staticmethod
    def screenshot(filename=None) -> Path:
        return Screenshot.capture(filename)

    # -------------------------
    # Apps
    # -------------------------

    @staticmethod
    def open(package: str):
        AppManager.open(package)

    @staticmethod
    def close(package: str):
        AppManager.close(package)

    @staticmethod
    def is_installed(package: str):
        return AppManager.is_installed(package)

    # -------------------------
    # Recorder
    # -------------------------

    @staticmethod
    def record_start():
        Recorder.start()

    @staticmethod
    def record_stop():
        Recorder.stop()

    @staticmethod
    def record_pull():
        return Recorder.pull()