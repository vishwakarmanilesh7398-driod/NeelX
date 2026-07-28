"""
=========================================
Project : NeelX
Module  : Plugin Loader
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.logger.logger import NeelLogger
from core.plugins.manager import PluginManager


class PluginLoader:
    """
    Handles loading and unloading of plugins.
    """

    @classmethod
    def load_plugins(cls):

        NeelLogger.info("Loading Plugins...")

        PluginManager.load_all()

        NeelLogger.success("Plugins Loaded Successfully.")

    @classmethod
    def unload_plugins(cls):

        NeelLogger.info("Unloading Plugins...")

        PluginManager.unload_all()

        NeelLogger.success("Plugins Unloaded Successfully.")