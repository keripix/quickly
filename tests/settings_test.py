#!/usr/bin/env python

import unittest
import os
import quickly.settings as settings


class SettingsTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'testsettings.ini')

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def testDefaultSettingsPath(self):
        default = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'settings.ini')
        backup = os.path.join(os.path.dirname(default), '_settings.ini')

        if os.path.exists(default):
            os.rename(default, backup)

        settings.Settings()

        self.assertTrue(os.path.exists(default))

        if (os.path.exists(backup)):
            os.remove(default)
            os.rename(backup, default)

    def testInitiatingQuicklyTheFirstTimeWouldCreateSettingsFile(self):
        settings.Settings(self.path)

        settingPath = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'testsettings.ini')
        self.assertTrue(os.path.exists(settingPath))

    def testGetSettings(self):
        s = settings.Settings(self.path)
        config = s.getConfig()

        self.assertEqual(config['DEFAULT']['name'], 'quickly')

    def testWritingSettings(self):
        s = settings.Settings(self.path)
        config = s.getConfig()

        # write something new
        config['PATH'] = {'python': "/some/path/python", 'php': "/some/path/php"}
        s.writeConfig(config)

        # now test wether the last config has been saved properly
        c = s.getConfig()
        self.assertTrue(c['PATH']['python'], "/some/path/python")

    def testDeleteConfigKey(self):
        s = settings.Settings(self.path)
        config = s.getConfig()

        # write something new
        config['PATH'] = {'python': "/some/path/python", 'php': "/some/path/php"}
        s.writeConfig(config)
        config = s.getConfig()

        # lets delete something
        config.remove_option('PATH', 'python')
        s.writeConfig(config)
        config = s.getConfig()

        self.assertFalse('python' in config['PATH'])
        self.assertTrue('php' in config['PATH'])


if __name__ == '__main__':
    unittest.main()
