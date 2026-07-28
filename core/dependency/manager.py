"""
=========================================
Project : NeelX
Module  : Dependency Manager
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

import importlib

from core.logger.logger import NeelLogger
from core.dependency.dependency import Dependency


class DependencyManager:

    _dependencies = []

    @classmethod
    def register(cls, dependency: Dependency):

        cls._dependencies.append(dependency)

        NeelLogger.info(
            f"Dependency Registered -> {dependency.name}"
        )

    @classmethod
    def check_all(cls):

        NeelLogger.info("Checking Dependencies...")

        for dependency in cls._dependencies:

            try:

                importlib.import_module(
                    dependency.package
                )

                dependency.installed = True

                NeelLogger.success(
                    f"{dependency.name} Installed"
                )

            except ImportError:

                dependency.installed = False

                NeelLogger.error(
                    f"{dependency.name} Missing"
                )

        NeelLogger.info("Dependency Check Finished.")

    @classmethod
    def installed(cls):

        return [
            dep.info()
            for dep in cls._dependencies
            if dep.installed
        ]

    @classmethod
    def missing(cls):

        return [
            dep.info()
            for dep in cls._dependencies
            if not dep.installed
        ]

    @classmethod
    def count(cls):

        return len(cls._dependencies)

    @classmethod
    def clear(cls):

        cls._dependencies.clear()

        NeelLogger.warning(
            "Dependency List Cleared."
        )