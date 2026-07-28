"""
=========================================
Project : NeelX
Module  : Engine
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.logger.logger import NeelLogger
from core.config.config import ConfigManager

from core.events.events import EventBus
from core.events.event_types import SYSTEM_START

from core.engine.state import EngineState

# Services
from core.services.manager import ServiceManager
from core.services.registry import (
    AndroidService,
    VoiceService,
    VisionService,
    AutomationService,
)

# Plugins
from core.plugins.manager import PluginManager
from core.plugins.loader import PluginLoader
from plugins.demo.demo_plugin import DemoPlugin

# Dependencies
from core.dependency.manager import DependencyManager
from core.dependency.registry import DEPENDENCIES


class NeelEngine:

    _state = EngineState.STOPPED

    @classmethod
    def start(cls):

        if cls._state == EngineState.RUNNING:
            NeelLogger.warning("Engine is already running.")
            return

        cls._state = EngineState.STARTING

        # -------------------------
        # Initialize Core
        # -------------------------

        NeelLogger.initialize()
        ConfigManager.initialize()

        NeelLogger.system("NeelX Starting...")
        NeelLogger.info("Initializing Core...")

        # -------------------------
        # Dependency Check
        # -------------------------

        for dependency in DEPENDENCIES:
            DependencyManager.register(dependency)

        DependencyManager.check_all()

        # -------------------------
        # Register Services
        # -------------------------

        ServiceManager.register(AndroidService())
        ServiceManager.register(VoiceService())
        ServiceManager.register(VisionService())
        ServiceManager.register(AutomationService())

        ServiceManager.start_all()

        # -------------------------
        # Register Plugins
        # -------------------------

        PluginManager.register(DemoPlugin())

        PluginLoader.load_plugins()

        # -------------------------
        # Fire Startup Event
        # -------------------------

        EventBus.emit(
            SYSTEM_START,
            {
                "version": "0.7.0",
                "status": "Running"
            }
        )

        cls._state = EngineState.RUNNING

        NeelLogger.success("NeelEngine Started Successfully.")

    @classmethod
    def stop(cls):

        if cls._state == EngineState.STOPPED:
            return

        PluginLoader.unload_plugins()

        ServiceManager.stop_all()

        cls._state = EngineState.STOPPED

        NeelLogger.system("NeelEngine Stopped.")

    @classmethod
    def restart(cls):

        cls.stop()
        cls.start()

    @classmethod
    def status(cls):

        return cls._state.value