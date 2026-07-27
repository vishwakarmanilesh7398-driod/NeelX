"""
=========================================
Project : NeelX
Module  : Logger
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from datetime import datetime
from pathlib import Path


class NeelLogger:
    """
    NeelX Custom Logger
    """

    LOG_DIR = Path("logs")
    LOG_FILE = LOG_DIR / "neelx.log"

    @classmethod
    def initialize(cls):
        """
        Create log directory and log file.
        """
        cls.LOG_DIR.mkdir(exist_ok=True)

        if not cls.LOG_FILE.exists():
            cls.LOG_FILE.touch()

    @classmethod
    def _write(cls, level: str, message: str):
        """
        Internal logging function.
        """

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = f"[{timestamp}] [{level}] {message}"

        print(log_message)

        with open(cls.LOG_FILE, "a", encoding="utf-8") as log:
            log.write(log_message + "\n")

    @classmethod
    def info(cls, message):
        cls._write("INFO", message)

    @classmethod
    def warning(cls, message):
        cls._write("WARNING", message)

    @classmethod
    def error(cls, message):
        cls._write("ERROR", message)

    @classmethod
    def success(cls, message):
        cls._write("SUCCESS", message)

    @classmethod
    def system(cls, message):
        cls._write("SYSTEM", message)

    @classmethod
    def android(cls, message):
        cls._write("ANDROID", message)

    @classmethod
    def vision(cls, message):
        cls._write("VISION", message)

    @classmethod
    def voice(cls, message):
        cls._write("VOICE", message)

    @classmethod
    def gesture(cls, message):
        cls._write("GESTURE", message)

    @classmethod
    def automation(cls, message):
        cls._write("AUTOMATION", message)