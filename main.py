from core.logger.logger import NeelLogger
from core.config.config import ConfigManager
from core.events.events import EventBus
from core.events.event_types import SYSTEM_START


def on_system_start(data):
    print()
    print("🚀 NeelX Event Working")
    print(data)


def main():

    NeelLogger.initialize()
    ConfigManager.initialize()

    NeelLogger.system("NeelX Starting...")
    NeelLogger.info("Loading Modules")
    NeelLogger.success("Logger Initialized Successfully")
    NeelLogger.android("Android Module Ready")
    NeelLogger.voice("Voice Module Loaded")
    NeelLogger.gesture("Gesture Engine Loaded")
    NeelLogger.vision("Vision Engine Loaded")
    NeelLogger.automation("Automation Engine Loaded")

    # Register Event
    EventBus.subscribe(
        SYSTEM_START,
        on_system_start
    )

    # Fire Event
    EventBus.emit(
        SYSTEM_START,
        {
            "version": "1.0.0",
            "status": "Running"
        }
    )


if __name__ == "__main__":
    main()