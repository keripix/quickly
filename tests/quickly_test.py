#!/usr/bin/env python

import unittest
import os
from quickly.quickly import Quickly


class QuicklyTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.path.expanduser('~'), '.config', 'quickly', 'testsettings.ini')

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def testInitQuickly(self):
        q = Quickly(self.path)
        self.assertEqual(q.config['DEFAULT']['name'], "quickly")

    def testSettingExistingPath(self):
        q = Quickly(self.path)
        q.add('javascript', os.path.dirname(self.path))

        self.assertTrue(q.config['PATH']['javascript'], os.path.dirname(self.path))

    def testSettingNonExistingPath(self):
        q = Quickly(self.path)

        self.assertRaises(OSError, q.add, 'javascript', '/some/non/existing/path')

    def testDeletingKey(self):
        q = Quickly(self.path)
        q.add('javascript', os.path.dirname(self.path))
        q.add('php', os.path.dirname(self.path))
        q.add('python', os.path.dirname(self.path))

        self.assertTrue('python' in q.config['PATH'])

        # now delete something
        q.remove('php')
        self.assertFalse('php' in q.config['PATH'])
        self.assertTrue('python' in q.config['PATH'])

    def testSyncing(self):
        q = Quickly(self.path)
        q.add('javascript', os.path.dirname(self.path))
        q.add('php', os.path.dirname(self.path))
        q.add('python', os.path.dirname(self.path))

        self.assertTrue('python' in q.config['PATH'])

        q.remove('php')
        q.sync()

        q2 = Quickly(self.path)
        self.assertTrue('python' in q2.config['PATH'])
        self.assertTrue('javascript' in q2.config['PATH'])

if __name__ == '__main__':
    unittest.main()
