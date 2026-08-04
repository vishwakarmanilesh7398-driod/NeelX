"""
=========================================
Project : NeelX
Module  : Android Screen
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import os

from android.adb import ADB


class Screen:

    @staticmethod
    def screenshot(path: str = "data/screenshot.png"):

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        remote_path = "/sdcard/neelx_screen.png"

        print("📸 Capturing Android screen...")

        ADB.shell(
            f"screencap -p {remote_path}"
        )

        ADB.pull(
            remote_path,
            path
        )

        ADB.shell(
            f"rm {remote_path}"
        )

        print(f"✅ Screenshot saved: {path}")

        return path

