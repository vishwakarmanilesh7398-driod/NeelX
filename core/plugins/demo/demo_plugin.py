"""
=========================================
Project : NeelX
Module  : Demo Plugin
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.logger.logger import NeelLogger
from core.plugins.plugin import BasePlugin


class DemoPlugin(BasePlugin):

    def __init__(self):
        super().__init__(
            name="DemoPlugin",
            version="1.0.0"
        )

    def load(self):

        self.loaded = True

        NeelLogger.success(
            "Demo Plugin Loaded"
        )

    def unload(self):

        self.loaded = False

        NeelLogger.warning(
            "Demo Plugin Unloaded"
        )