from voice.microphone import Microphone

recognizer, microphone = Microphone.create()

print("✅ Microphone Ready")
print(type(recognizer))
print(type(microphone))