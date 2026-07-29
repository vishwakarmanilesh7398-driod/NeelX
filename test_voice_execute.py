from voice.listener import VoiceListener
from neelx.api import NeelX

text = VoiceListener.listen()

print("\nRecognized :", text)

if text:
    print("\nExecuting...")
    NeelX.execute(text)

print("\n✅ Finished")