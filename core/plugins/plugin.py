"""
=========================================
Project : NeelX
Module  : Base Plugin
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from abc import ABC, abstractmethod


class BasePlugin(ABC):
    """
    Base class for all NeelX plugins.
    """

    def __init__(self, name: str, version: str = "1.0.0"):
        self.name = name
        self.version = version
        self.loaded = False

    @abstractmethod
    def load(self):
        """
        Load plugin resources.
        """
        pass

    @abstractmethod
    def unload(self):
        """
        Unload plugin resources.
        """
        pass

    def is_loaded(self) -> bool:
        """
        Returns plugin status.
        """
        return self.loaded

    def info(self) -> dict:
        """
        Returns plugin information.
        """
        return {
            "name": self.name,
            "version": self.version,
            "loaded": self.loaded
        }