#!/usr/bin/env python


import unittest
from quickly.settings import Settings
import os
import platform
import sys


class TestSetting(unittest.TestCase):
    def setUp(self):
        if sys.platform.startswith('win') or sys.platform.startswith('cyg'):
            self.path = os.path.join(os.getenv('HOME'), 'config', "testsetting")
        else:
            self.path = os.path.join(os.getenv('HOME'), '.config', "testsetting")

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def testInit(self):
        s = Settings("testsetting")
        self.assertEqual(s.name, "testsetting")

    def testLoadSettings(self):
        pass

    def testWriteSettings(self):
        Settings("testsetting")
        self.assertTrue(os.path.exists(self.path))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSetting)
    unittest.TextTestRunner(verbosity=2).run(suite)
