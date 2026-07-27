"""
=========================================
Project : NeelX
Module  : Base Service
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from abc import ABC, abstractmethod


class BaseService(ABC):
    """
    Base class for all NeelX services.
    """

    def __init__(self, name: str):
        self.name = name
        self.running = False

    @abstractmethod
    def start(self):
        """
        Start the service.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Stop the service.
        """
        pass

    def status(self) -> bool:
        """
        Return current service status.
        """
        return self.running