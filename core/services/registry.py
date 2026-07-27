"""
=========================================
Project : NeelX
Module  : Service Registry
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from core.logger.logger import NeelLogger
from core.services.service import BaseService


class AndroidService(BaseService):

    def __init__(self):
        super().__init__("Android")

    def start(self):
        self.running = True
        NeelLogger.android("Android Service Started")

    def stop(self):
        self.running = False
        NeelLogger.android("Android Service Stopped")


class VoiceService(BaseService):

    def __init__(self):
        super().__init__("Voice")

    def start(self):
        self.running = True
        NeelLogger.voice("Voice Service Started")

    def stop(self):
        self.running = False
        NeelLogger.voice("Voice Service Stopped")


class VisionService(BaseService):

    def __init__(self):
        super().__init__("Vision")

    def start(self):
        self.running = True
        NeelLogger.vision("Vision Service Started")

    def stop(self):
        self.running = False
        NeelLogger.vision("Vision Service Stopped")


class AutomationService(BaseService):

    def __init__(self):
        super().__init__("Automation")

    def start(self):
        self.running = True
        NeelLogger.automation("Automation Service Started")

    def stop(self):
        self.running = False
        NeelLogger.automation("Automation Service Stopped")