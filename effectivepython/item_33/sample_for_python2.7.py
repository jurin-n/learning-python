# -*- coding: utf-8 -*-
"""
 メタクラスの動作を確認するためのサンプルコード。
"""
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object):
    __metaclass__ = Meta
    stuff = 123

    def foo(self):
        pass

obj = MyClass()
