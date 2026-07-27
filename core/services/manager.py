"""
=========================================
Project : NeelX
Module  : Service Manager
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.logger.logger import NeelLogger
from core.services.service import BaseService


class ServiceManager:
    """
    Manages all NeelX services.
    """

    _services = {}

    @classmethod
    def register(cls, service: BaseService):

        cls._services[service.name] = service

        NeelLogger.success(
            f"Service Registered -> {service.name}"
        )

    @classmethod
    def unregister(cls, name: str):

        if name in cls._services:

            del cls._services[name]

            NeelLogger.warning(
                f"Service Removed -> {name}"
            )

    @classmethod
    def get(cls, name: str):

        return cls._services.get(name)

    @classmethod
    def start_all(cls):

        for service in cls._services.values():

            service.start()

        NeelLogger.info("All Services Started")

    @classmethod
    def stop_all(cls):

        for service in cls._services.values():

            service.stop()

        NeelLogger.info("All Services Stopped")

    @classmethod
    def list_services(cls):

        return list(cls._services.keys())

    @classmethod
    def count(cls):

        return len(cls._services)