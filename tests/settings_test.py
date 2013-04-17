#!/usr/bin/env python

import unittest
import os
import quickly.settings as settings


class QuicklyTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'testsettings.ini')

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def testInitiatingQuicklyTheFirstTimeWouldCreateSettingsFile(self):
        settings.Settings(self.path)

        settingPath = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'testsettings.ini')
        self.assertTrue(os.path.exists(settingPath))

    def testGetSettings(self):
        s = settings.Settings(self.path)
        config = s.getConfig()

        self.assertEqual(config['DEFAULT']['name'], 'quickly')


if __name__ == '__main__':
    unittest.main()
