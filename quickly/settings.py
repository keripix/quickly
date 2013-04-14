#!/usr/bin/env python


import configparser
import os
import sys


class Settings:
    """
    Settings' responsibility is to read/write setting from a given application.
    The path to read/write is the user's home directory
    """

    def __init__(self, name):
        self.name = name
        self.conf = configparser.ConfigParser()
        self.conf['DEFAULT']['name'] = name

        if sys.platform.startswith('win') or sys.platform.startswith('cyg'):
            self.path = os.path.join(os.getenv('HOME'), 'config', name)
        else:
            self.path = os.path.join(os.getenv('HOME'), '.config', name)

        self.createSettings()

    def set(self, key=None, value=None):
        if key is None or value is None:
            raise NameError("Key or Value cannot be None")

    def writeSettings(self):
        pass

    def createSettings(self):
        """
        First, it will check wether the default path exists.

        If the default path is found to be a directory, then it will
        raise an exception.

        If the config file has not been created, than this method will
        create it.
        """
        if os.path.isdir(self.path):
            raise OSError("The {0} is a directory. We are unable to create a config file. Exiting".format(self.path))

        if not os.path.exists(self.path):
            # Create config
            with open(self.path, 'w') as configfile:
                self.conf.write(configfile)
