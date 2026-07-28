"""
=========================================
Project : NeelX
Module  : Dependency
Author  : Nilesh Vishwakarma
Version : 1.0.0
=========================================
"""


class Dependency:

    def __init__(
        self,
        name: str,
        package: str,
        required: bool = True
    ):

        self.name = name
        self.package = package
        self.required = required
        self.installed = False

    def info(self):

        return {
            "name": self.name,
            "package": self.package,
            "required": self.required,
            "installed": self.installed
        }