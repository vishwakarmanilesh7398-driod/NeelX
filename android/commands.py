"""
=========================================
Project : NeelX
Module  : Android Commands
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

ADB_VERSION = ["adb", "version"]

ADB_DEVICES = ["adb", "devices"]

DEVICE_MODEL = [
    "adb",
    "shell",
    "getprop",
    "ro.product.model",
]

ANDROID_VERSION = [
    "adb",
    "shell",
    "getprop",
    "ro.build.version.release",
]

DEVICE_BRAND = [
    "adb",
    "shell",
    "getprop",
    "ro.product.brand",
]

BATTERY = [
    "adb",
    "shell",
    "dumpsys",
    "battery",
]

SCREEN_SIZE = [
    "adb",
    "shell",
    "wm",
    "size",
]