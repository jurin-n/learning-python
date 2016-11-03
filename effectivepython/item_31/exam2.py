# -*- coding: utf-8 -*-
from grade import Grade

class Exam2(object):
    # クラス属性
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

exam = Exam2()
exam.writing_grade = 100
print(exam.writing_grade)
    