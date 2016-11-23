# -*- coding: utf-8 -*-

from unittest import TestCase, main, skip
from sample import to_str, to_unicode

class SampleTestCase(TestCase):
    # @skip('test')
    def test_to_str_change_unicode_to_str(self):
        self.assertEqual(to_str(unicode(u'\u592a\u90ce')), '太郎')

    def test_to_str_change_str_to_str(self):
        self.assertEqual(to_str('太郎'), '太郎')

    def test_to_unicode_change_str_to_unicode(self):
        self.assertEqual(to_unicode('太郎'), unicode(u'\u592a\u90ce'))
        
    def test_to_unicode_change_unicode_to_unicode(self):
        self.assertEqual(to_unicode(unicode(u'\u592a\u90ce')), unicode(u'\u592a\u90ce'))

if __name__ == '__main__':
    main()
