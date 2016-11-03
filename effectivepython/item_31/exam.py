# -*- coding: utf-8 -*-
class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0
    
    @staticmethod
    def _check_grade(value):
        if not(0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
    
    @property
    def writing_grade(self):
        return self._writing_grade
    
    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value
    
    @property
    def math_grade(self):
        return self._math_grade
    
    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value

exam = Exam()
exam.writing_grade = 40
print(exam.writing_grade)
exam.writing_grade = 101
print(exam.writing_grade)

#exam.math_grade = 40
#print(exam.math_grade)
#exam.math_grade = 101
#print(exam.math_grade)
