from core.logger.logger import NeelLogger


def main():

    NeelLogger.initialize()

    NeelLogger.system("NeelX Starting...")

    NeelLogger.info("Loading Modules")

    NeelLogger.success("Logger Initialized Successfully")

    NeelLogger.android("Android Module Ready")

    NeelLogger.voice("Voice Module Loaded")

    NeelLogger.gesture("Gesture Engine Loaded")

    NeelLogger.vision("Vision Engine Loaded")

    NeelLogger.automation("Automation Engine Loaded")


if __name__ == "__main__":
    main()