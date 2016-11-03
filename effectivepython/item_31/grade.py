# -*- coding: utf-8 -*-
from weakref import WeakKeyDictionary

class Grade(object):
    def __init__(self):
        self._value = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._value.get(instance, 0)
    
    def __set__(self, instance, value):
        if not(0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        print('[DEBUG]', instance)
        self._value[instance] = value
