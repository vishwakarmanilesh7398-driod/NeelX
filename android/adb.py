"""
=========================================
Project : NeelX
Module  : ADB Wrapper
Author  : Nilesh Vishwakarma
Version : 1.1.0
=========================================
"""

import subprocess
from pathlib import Path

from android.exceptions import (
    ADBNotFoundError,
    CommandExecutionError,
)


class ADB:

    ROOT = Path(__file__).resolve().parent.parent
    ADB_PATH = ROOT / "tools" / "platform-tools" / "adb.exe"

    @classmethod
    def execute(cls, command: list[str]) -> str:

        if not cls.ADB_PATH.exists():
            raise ADBNotFoundError(
                f"ADB not found: {cls.ADB_PATH}"
            )

        command = [str(cls.ADB_PATH)] + command[1:]

        try:

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True
            )

            return result.stdout.strip()

        except subprocess.CalledProcessError as error:

            raise CommandExecutionError(
                error.stderr.strip()
            )

    @classmethod
    def version(cls):

        return cls.execute(
            ["adb", "version"]
        )

    @classmethod
    def devices(cls):

        return cls.execute(
            ["adb", "devices"]
        )

    @classmethod
    def shell(cls, cmd: str):

        return cls.execute(
            ["adb", "shell", cmd]
        )

    @classmethod
    def pull(cls, remote_path: str, local_path: str):

        return cls.execute(
            ["adb", "pull", remote_path, local_path]
        )

