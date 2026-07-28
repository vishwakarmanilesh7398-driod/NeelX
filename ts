[1mdiff --git a/core/commands/executor.py b/core/commands/executor.py[m
[1mindex e69de29..098fe96 100644[m
[1m--- a/core/commands/executor.py[m
[1m+++ b/core/commands/executor.py[m
[36m@@ -0,0 +1,51 @@[m
[32m+[m[32m"""[m
[32m+[m[32m=========================================[m
[32m+[m[32mProject : NeelX[m
[32m+[m[32mModule  : Command Executor[m
[32m+[m[32mAuthor  : Nilesh Vishwakarma[m
[32m+[m[32mVersion : 1.0.0[m
[32m+[m[32m=========================================[m
[32m+[m[32m"""[m
[32m+[m
[32m+[m[32mfrom core.commands.command import Command[m
[32m+[m[32mfrom core.apps.manager import Apps[m
[32m+[m[32mfrom android.api import Android[m
[32m+[m
[32m+[m
[32m+[m[32mclass CommandExecutor:[m
[32m+[m
[32m+[m[32m    @staticmethod[m
[32m+[m[32m    def execute(command: Command):[m
[32m+[m
[32m+[m[32m        action = command.action[m
[32m+[m[32m        target = command.target[m
[32m+[m
[32m+[m[32m        # -------------------------[m
[32m+[m[32m        # Apps[m
[32m+[m[32m        # -------------------------[m
[32m+[m
[32m+[m[32m        if action == "open":[m
[32m+[m[32m            Apps.open(target)[m
[32m+[m[32m            return True[m
[32m+[m
[32m+[m[32m        if action == "close":[m
[32m+[m[32m            Apps.close(target)[m
[32m+[m[32m            return True[m
[32m+[m
[32m+[m[32m        # -------------------------[m
[32m+[m[32m        # Navigation[m
[32m+[m[32m        # -------------------------[m
[32m+[m
[32m+[m[32m        if action == "home":[m
[32m+[m[32m            Android.home()[m
[32m+[m[32m            return True[m
[32m+[m
[32m+[m[32m        if action == "back":[m
[32m+[m[32m            Android.back()[m
[32m+[m[32m            return True[m
[32m+[m
[32m+[m[32m        if action == "recent":[m
[32m+[m[32m            Android.recent()[m
[32m+[m[32m            return True[m
[32m+[m
[32m+[m[32m        raise ValueError(f"Unknown command: {action}")[m
\ No newline at end of file[m
