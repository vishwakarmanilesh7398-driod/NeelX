from core.engine.engine import NeelEngine
from core.events.events import EventBus
from core.events.event_types import SYSTEM_START


def on_system_start(data):

    print()

    print("🚀 NeelX Event Working")

    print(data)


EventBus.subscribe(
    SYSTEM_START,
    on_system_start
)


if __name__ == "__main__":
    NeelEngine.start()