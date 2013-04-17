#!/usr/bin/env python

import os
import configparser


class Settings:
    def __init__(self, path=None):
        if path is None:
            self.path = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'settings.ini')
        else:
            self.path = path

        self.checkSettings()

    def getConfig(self):
        config = configparser.ConfigParser()
        config.read(self.path)
        return config

    def writeConfig(self, config):
        with open(self.path, 'w') as configFile:
            config.write(configFile)

    def checkSettings(self):
        if not os.path.exists(os.path.dirname(self.path)):
            os.makedirs(os.path.dirname(self.path))

        if os.path.exists(self.path):
            return

        config = configparser.ConfigParser()
        config['DEFAULT'] = {'name': 'quickly'}

        with open(self.path, 'w') as file:
            config.write(file)
