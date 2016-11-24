# -*- coding: utf-8 -*-
import unittest
from unittest.runner import TextTestResult
TextTestResult.getDescription = lambda _, test: test.shortDescription()

class SimpleTest(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    
    def test_pass(self):
        '''ああああ
        '''
        self.assertEqual(10, 7 + 3)

    def test_fail(self):
        self.assertEqual(11, 7 + 3)
