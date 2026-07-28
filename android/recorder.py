"""
=========================================
Project : NeelX
Module  : Screen Recorder
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from pathlib import Path
from datetime import datetime
import subprocess

from android.adb import ADB


class Recorder:

    REMOTE_PATH = "/sdcard/neelx_record.mp4"

    @staticmethod
    def start():

        subprocess.Popen(
            [
                str(ADB.ADB_PATH),
                "shell",
                "screenrecord",
                Recorder.REMOTE_PATH
            ]
        )

    @staticmethod
    def stop():

        subprocess.run(
            [
                str(ADB.ADB_PATH),
                "shell",
                "pkill",
                "-INT",
                "screenrecord"
            ]
        )

    @staticmethod
    def pull(filename: str = None):

        recordings = Path("temp") / "recordings"
        recordings.mkdir(parents=True, exist_ok=True)

        if filename is None:

            filename = (
                datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                + ".mp4"
            )

        destination = recordings / filename

        subprocess.run(
            [
                str(ADB.ADB_PATH),
                "pull",
                Recorder.REMOTE_PATH,
                str(destination)
            ],
            check=True
        )

        return destination