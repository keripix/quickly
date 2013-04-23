#!/usr/bin/env python

import quickly.settings as settings
import os


class Quickly:
    def __init__(self, path=None):
        self.setting = settings.Settings(path)
        self.config = self.setting.getConfig()

    def add(self, key, path):
        if not os.path.exists(path):
            raise OSError("{0} does not exists".format(path))

        self.config['PATH'][key] = path

    def remove(self, key):
        self.config.remove_option('PATH', key)

    def sync(self):
        self.setting.writeConfig(self.config)

QUICKLY_PARSER = {
    "prog": "quickly",
    "description": "A small script that allows you to do cd without having to type the whole path",
    "args": [
        {
            "name": "addDirectory",
            "type": "positional",
            "help": "Add directory to be rembered",
            ""
        },
        {
            "name": "directoryKey",
            "type": "positional",
            "help": "The directory will be accessed by this key"
        }
    ]
}

if __name__ == '__main__':
    pass
    # TODO args parser
    # TODO autocompleter
