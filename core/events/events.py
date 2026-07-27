"""
=========================================
Project : NeelX
Module  : Event Bus
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from collections import defaultdict

from core.logger.logger import NeelLogger


class EventBus:

    _listeners = defaultdict(list)

    @classmethod
    def subscribe(cls, event_name, callback):

        cls._listeners[event_name].append(callback)

        NeelLogger.info(
            f"Subscribed -> {event_name}"
        )

    @classmethod
    def emit(cls, event_name, data=None):

        NeelLogger.info(
            f"Event -> {event_name}"
        )

        for callback in cls._listeners[event_name]:

            callback(data)

    @classmethod
    def unsubscribe(cls, event_name, callback):

        if callback in cls._listeners[event_name]:

            cls._listeners[event_name].remove(callback)

            NeelLogger.info(
                f"Unsubscribed -> {event_name}"
            )

    @classmethod
    def clear(cls):

        cls._listeners.clear()

        NeelLogger.info("All Events Cleared")

    @classmethod
    def listener_count(cls):

        return sum(
            len(value)
            for value in cls._listeners.values()
        )