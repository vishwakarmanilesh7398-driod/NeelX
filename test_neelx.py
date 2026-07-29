from neelx.api import NeelX

print("Opening Settings...")
NeelX.execute("please open settings")

print("Going Home...")
NeelX.execute("go home")

print("Opening Chrome...")
NeelX.execute("launch chrome")

print("Going Back...")
NeelX.execute("go back")

print("Taking Screenshot...")
NeelX.execute("please capture")

print("✅ Done")