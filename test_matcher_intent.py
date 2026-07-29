from core.intent.matcher import IntentMatcher


tests = [

    "open settings",
    "launch chrome",
    "start youtube",
    "run instagram",

    "close chrome",
    "exit settings",

    "home",
    "back",

    "capture",
    "screenshot"

]


for text in tests:

    intent = IntentMatcher.match(text)

    print(f"{text:20} -> {intent}")