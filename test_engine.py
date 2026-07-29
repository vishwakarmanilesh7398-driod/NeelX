from core.intent.engine import IntentEngine

tests = [
    "open settings",
    "launch chrome",
    "run youtube",
    "start instagram",
    "close settings",
    "home",
    "back",
    "capture"
]

for text in tests:
    intent = IntentEngine.understand(text)
    print(f"{text:20} -> {intent}")