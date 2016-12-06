# -*- coding: utf-8 -*-
import unittest
from unittest.runner import TextTestResult
TextTestResult.getDescription = lambda _, test: test.shortDescription()

def setUpModule():
    print('[DEBUG]setUpModule')

def tearDownModule():
    print('[DEBUG]tearDownModule')

class SimpleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('[DEBUG]setUpClass start')
        cls.setup_class = 'SET UP CLASS!'
        print('[DEBUG]setUpClass end')

    @classmethod
    def tearDownClass(cls):
        print('[DEBUG]tearDownClass start')
        cls.setup_class = ''
        print('[DEBUG]tearDownClass end')

    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        print("cls.setup_class=%s" , self.setup_class)
        self.fail("shouldn't happen")

    
    def test_pass(self):
        '''ああああ
        '''
        print("cls.setup_class=" + self.setup_class)
        self.assertEqual(10, 7 + 3)

    def test_fail(self):
        self.assertEqual(11, 7 + 3)
        
if __name__ == '__main__':
    unittest.main()
