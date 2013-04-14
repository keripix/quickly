#!/usr/bin/env python


import unittest
from quickly.settings import Settings
from os.path import exists
import os
import platform


class TestSetting(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLoadSettings(self):
        pass

    def testWriteSettings(self):
        Settings("testsetting")

        if (platform.system() == 'Linux'):
            self.assertTrue(exists(os.getenv('HOME') + '/.config/testSetting'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSetting)
    unittest.TextTestRunner(verbosity=2).run(suite)
