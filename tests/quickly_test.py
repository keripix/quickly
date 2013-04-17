#!/usr/bin/env python

import unittest
import os
import quickly.quickly as quickly


class QuicklyTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'testsettings.ini')

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def testInitQuickly(self):
        q = quickly.Quickly(self.path)
        self.assertEqual(q.config['DEFAULT']['name'], "quickly")

    def testSettingExistingPath(self):
        q = quickly.Quickly(self.path)
        q.add('javascript', os.path.dirname(self.path))

        self.assertTrue(q.config['PATH']['javascript'], os.path.dirname(self.path))

    def testSettingNonExistingPath(self):
        q = quickly.Quickly(self.path)

        self.assertRaises(OSError, q.add, 'javascript', '/some/non/existing/path')

if __name__ == '__main__':
    unittest.main()
