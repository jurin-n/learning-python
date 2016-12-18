# -*- coding: utf-8 -*-

# 属性とカラム名を連携するディスクリプタを定義
class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer(object):
    # クラス属性
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')

foo = Customer()
print('Before:', repr(foo.first_name), foo.__dict__, Customer.__dict__['first_name'])
foo.first_name = 'test taro'
print('After:', repr(foo.first_name), foo.__dict__, Customer.__dict__['first_name'])
