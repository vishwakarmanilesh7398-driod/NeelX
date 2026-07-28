from vision.actions import VisionActions

success = VisionActions.click(
    "vision/templates/settings_icon.png"
)

if success:
    print("✅ Vision Click Success")
else:
    print("❌ Template Not Found")