from core.ai.chat import ChatEngine

tests = [

    "how are you",
    "who are you",
    "thanks",
    "good morning",
    "hello"

]

for text in tests:

    print(text, "->", ChatEngine.reply(text))