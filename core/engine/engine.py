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

from core.services.manager import ServiceManager
from core.services.registry import (
    AndroidService,
    VoiceService,
    VisionService,
    AutomationService,
)


class NeelEngine:

    _state = EngineState.STOPPED

    @classmethod
    def start(cls):

        if cls._state == EngineState.RUNNING:
            NeelLogger.warning("Engine is already running.")
            return

        cls._state = EngineState.STARTING

        # Initialize Core
        NeelLogger.initialize()
        ConfigManager.initialize()

        NeelLogger.system("NeelX Starting...")
        NeelLogger.info("Loading Modules")
        NeelLogger.success("Logger Initialized Successfully")

        # Register Services
        ServiceManager.register(AndroidService())
        ServiceManager.register(VoiceService())
        ServiceManager.register(VisionService())
        ServiceManager.register(AutomationService())

        # Start All Services
        ServiceManager.start_all()

        # Fire Startup Event
        EventBus.emit(
            SYSTEM_START,
            {
                "version": "1.0.0",
                "status": "Running"
            }
        )

        cls._state = EngineState.RUNNING

        NeelLogger.success("NeelEngine Started Successfully.")

    @classmethod
    def stop(cls):

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