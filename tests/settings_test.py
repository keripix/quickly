#!/usr/bin/env python

import unittest
import os
import quickly.settings as settings


class QuicklyTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'settings.ini')

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def testInitiatingQuicklyTheFirstTimeWouldCreateSettingsFile(self):
        settings.Settings()

        settingPath = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'settings.ini')
        self.assertTrue(os.path.exists(settingPath))

if __name__ == '__main__':
    unittest.main()
