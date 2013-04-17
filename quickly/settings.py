#!/usr/bin/env python

import os
import configparser


class Settings:
    def __init__(self):
        self.path = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'settings.ini')
        return self.loadSettings()

    def loadSettings(self):
        self.checkSettings()

    def writeSettings(self, config):
        self.config

    def checkSettings(self):
        if not os.path.exists(os.path.dirname(self.path)):
            os.makedirs(os.path.dirname(self.path))

        if os.path.exists(self.path):
            return

        config = configparser.ConfigParser()
        config['DEFAULT'] = {'name': 'quickly'}

        with open(self.path, 'w') as file:
            config.write(file)
