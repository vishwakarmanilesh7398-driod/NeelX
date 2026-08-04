from core.ai.search import Search


tests = [
    "search free fire",
    "search free fire on youtube",
    "search free fire on google",
    "search free fire on chrome",
]


for text in tests:

    print(f"\nInput : {text}")

    result = Search.search(text)

    print(f"Output: {result}")