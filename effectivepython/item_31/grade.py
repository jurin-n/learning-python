# -*- coding: utf-8 -*-
class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value
    
    def __set__(self, instance, value):
        if not(0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value

