from core.ai.memory import Memory

Memory.set("name", "Nilesh")

print(Memory.get("name"))

Memory.clear()

print(Memory.get("name"))