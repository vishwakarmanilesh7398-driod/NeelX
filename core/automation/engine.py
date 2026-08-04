"""
=========================================
Project : NeelX
Module  : Automation Engine
Author  : Nilesh Vishwakarma
Version : 1.3.0
=========================================
"""

from core.commands.executor import CommandExecutor
from core.intent.nlp import NLP
from core.automation.parser import AutomationParser
from core.automation.router import AutomationRouter
from core.ai.brain import Brain


class AutomationEngine:

    @staticmethod
    def run(text):

        print("\n⚙️ Automation Started")

        actions = AutomationParser.parse(text)

        print(f"🧩 Actions Found: {len(actions)}")

        for action in actions:

            print(f"\n🚀 Executing: {action}")

            try:

                route = AutomationRouter.route(action)

                print(f"🧭 Route: {route}")

                # -------------------------
                # Android Command
                # -------------------------

                if route == "command":

                    intent = NLP.understand(action)

                    print(f"🧠 Intent: {intent}")

                    CommandExecutor.execute(intent)

                    print("✅ Command Completed")

                # -------------------------
                # Brain
                # -------------------------

                elif route == "brain":

                    reply = Brain.think(action)

                    print(f"🤖 Brain: {reply}")

                print("✅ Action Completed")

            except Exception as error:

                print(f"❌ Action Failed: {error}")

                return False

        print("\n✅ Automation Completed")

        return True