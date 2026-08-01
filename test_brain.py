from core.ai.brain import Brain

tests = [
    "how are you",
    "search free fire max",
    "calculate 25+75",      
    "what is today's date",
]

for text in tests:

    print(f"\nInput : {text}")

    result = Brain.think(text)

    print(f"Output : {result}")