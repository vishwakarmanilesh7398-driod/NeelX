"""
=========================================
Project : NeelX
Module  : Configuration Manager
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import json
from pathlib import Path

from core.config.defaults import DEFAULT_SETTINGS
from core.logger.logger import NeelLogger


class ConfigManager:
    """
    Handles loading, saving and accessing
    NeelX configuration.
    """

    SETTINGS_PATH = Path("config/settings.json")

    _settings = {}

    @classmethod
    def initialize(cls):
        """
        Initialize configuration system.
        """

        cls.SETTINGS_PATH.parent.mkdir(exist_ok=True)

        if not cls.SETTINGS_PATH.exists():

            cls._settings = DEFAULT_SETTINGS

            cls.save()

            NeelLogger.success("Default settings created.")

        else:

            cls.load()

            NeelLogger.info("Settings loaded.")

    @classmethod
    def load(cls):

        with open(cls.SETTINGS_PATH, "r", encoding="utf-8") as file:

            try:

                cls._settings = json.load(file)

            except json.JSONDecodeError:

                cls._settings = DEFAULT_SETTINGS

                cls.save()

                NeelLogger.warning(
                    "settings.json was invalid. Defaults restored."
                )

    @classmethod
    def save(cls):

        with open(cls.SETTINGS_PATH, "w", encoding="utf-8") as file:

            json.dump(
                cls._settings,
                file,
                indent=4
            )

    @classmethod
    def get(cls, path: str):

        data = cls._settings

        for key in path.split("."):

            data = data[key]

        return data

    @classmethod
    def set(cls, path: str, value):

        keys = path.split(".")

        data = cls._settings

        for key in keys[:-1]:

            data = data[key]

        data[keys[-1]] = value

        cls.save()

        NeelLogger.info(f"Config Updated : {path} -> {value}")