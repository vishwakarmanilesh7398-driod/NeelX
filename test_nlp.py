from core.intent.nlp import NLP

tests = [

    "please open settings",

    "can you launch chrome",

    "could you start youtube",

    "run instagram",

    "please close settings",

    "go home",

    "go back",

    "please capture"

]

for text in tests:

    intent = NLP.understand(text)

    print(f"{text:35} -> {intent}")