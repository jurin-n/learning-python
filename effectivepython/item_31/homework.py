# -*- coding: utf-8 -*-
class Homework(object):
    def __init__(self):
        self._grade = 0
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        if not(0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value

galileo = Homework()
galileo.grade = 95
print(galileo.grade)
galileo.grade = 101
print(galileo.grade)
