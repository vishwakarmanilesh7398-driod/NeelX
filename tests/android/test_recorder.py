"""
=========================================
Project : NeelX
Module  : Recorder Test
Author  : Nilesh Vishwakarma
Version : 1.1.0
=========================================
"""

import time

from android.device import AndroidDevice
from android.recorder import Recorder


def test_recorder():
    """
    Pytest test.
    """
    device = AndroidDevice()

    if not device.connect():
        raise RuntimeError("Device not connected")

    print("Connected :", device.model())

    print("Recording Started...")

    Recorder.start()

    time.sleep(10)

    print("Stopping Recording...")

    Recorder.stop()

    time.sleep(2)

    video = Recorder.pull()

    print("Saved :", video)

    assert video is not None


def main():
    """
    Manual execution.
    """
    test_recorder()


if __name__ == "__main__":
    main()