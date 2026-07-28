from android.device import AndroidDevice
from android.recorder import Recorder

import time

device = AndroidDevice()

device.connect()

print("Connected :", device.model())

print("Recording Started...")

Recorder.start()

time.sleep(10)

print("Stopping Recording...")

Recorder.stop()

time.sleep(2)

video = Recorder.pull()

print("Saved :", video)