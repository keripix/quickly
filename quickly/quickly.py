#!/usr/bin/env python

import quickly.settings as settings


class Quickly:
    def __init__(self):
        self.config = settings.Settings().getConfig()


if __name__ == '__main__':
    pass
