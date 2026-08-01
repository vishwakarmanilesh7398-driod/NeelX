"""
=========================================
Project : NeelX
Module  : Memory
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class Memory:

    _data = {}

    @classmethod
    def set(cls, key, value):

        cls._data[key] = value

    @classmethod
    def get(cls, key, default=None):

        return cls._data.get(key, default)

    @classmethod
    def clear(cls):

        cls._data.clear()