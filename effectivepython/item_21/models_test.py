# -*- coding: utf-8 -*-

from unittest import TestCase, main
from models import User

class UserTestCase(TestCase):
    def test_init_User(self):
        user = User(user_id='U001', name='山田太郎')
        
    def test_init_with_not_defined_field(self):
        with self.assertRaises(TypeError):
            user = User(not_defined_field='U001', name='山田太郎')

if __name__ == '__main__':
    main()
