#!/usr/bin/env python


class Settings:
    """
    Settings' responsibility is to read/write setting from a given application
    """

    def __init__(self, name):
        self.name = name

    def loadSettings(self):
        pass

    def writeSettings(self):
        pass
