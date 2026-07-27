"""
=========================================
Project : NeelX
Module  : Engine State
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""

from enum import Enum


class EngineState(Enum):
    STOPPED = "STOPPED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"