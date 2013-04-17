#!/usr/bin/env python

import quickly.settings as settings
import os


class Quickly:
    def __init__(self, path=None):
        self.config = settings.Settings(path).getConfig()

    def add(self, key, path):
        if not self.checkFile(path):
            raise OSError("{0} does not exists".format(path))

        self.config['PATH'][key] = path

    def checkFile(self, path):
        return os.path.exists(path)


if __name__ == '__main__':
    pass
