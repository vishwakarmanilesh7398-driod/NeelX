"""
=========================================
Project : NeelX
Module  : Screen Analyzer Test
=========================================
"""

from vision.screen_analyzer import ScreenAnalyzer


print()
print("👁️ NeelX Screen Analyzer Test")
print()

result = ScreenAnalyzer.analyze()

print()
print("=========================================")
print("✅ Analysis Completed")
print("=========================================")
print(f"📸 Screenshot : {result['screenshot']}")
print(f"📱 Package    : {result['package']}")
print()

