"""
=========================================
Project : NeelX
Module  : Plugin Manager
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.logger.logger import NeelLogger
from core.plugins.plugin import BasePlugin


class PluginManager:
    """
    Manages all NeelX plugins.
    """

    _plugins = {}

    @classmethod
    def register(cls, plugin: BasePlugin):

        cls._plugins[plugin.name] = plugin

        NeelLogger.success(
            f"Plugin Registered -> {plugin.name}"
        )

    @classmethod
    def unregister(cls, name: str):

        if name in cls._plugins:

            del cls._plugins[name]

            NeelLogger.warning(
                f"Plugin Removed -> {name}"
            )

    @classmethod
    def get(cls, name: str):

        return cls._plugins.get(name)

    @classmethod
    def load_all(cls):

        for plugin in cls._plugins.values():

            plugin.load()

        NeelLogger.info("All Plugins Loaded")

    @classmethod
    def unload_all(cls):

        for plugin in cls._plugins.values():

            plugin.unload()

        NeelLogger.info("All Plugins Unloaded")

    @classmethod
    def list_plugins(cls):

        return list(cls._plugins.keys())

    @classmethod
    def count(cls):

        return len(cls._plugins)