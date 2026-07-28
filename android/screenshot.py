"""
=========================================
Project : NeelX
Module  : Screenshot
Author  : Nilesh Vishwakarma
Version : 1.2.0
=========================================
"""

from pathlib import Path
from datetime import datetime
import subprocess
import shutil

from android.adb import ADB


class Screenshot:

    @staticmethod
    def capture(filename: str = None) -> Path:

        screenshot_dir = Path("temp") / "screenshots"
        screenshot_dir.mkdir(parents=True, exist_ok=True)

        if filename is None:
            filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"

        image_path = screenshot_dir / filename

        with open(image_path, "wb") as image:

            subprocess.run(
                [
                    str(ADB.ADB_PATH),
                    "exec-out",
                    "screencap",
                    "-p"
                ],
                stdout=image,
                check=True
            )

        # Latest screenshot copy
        latest = screenshot_dir / "latest.png"

        shutil.copy2(
            image_path,
            latest
        )

        return image_path