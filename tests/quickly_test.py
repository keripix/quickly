#!/usr/bin/env python

import unittest
import quickly.quickly as quickly


class QuicklyTest(unittest.TestCase):
    def testInitQuickly(self):
        q = quickly.Quickly()
        self.assertEqual(q.config['DEFAULT']['name'], "quickly")

if __name__ == '__main__':
    unittest.main()
