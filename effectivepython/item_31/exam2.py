# -*- coding: utf-8 -*-
from grade import Grade

class Exam2(object):
    # クラス属性
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

first_exam = Exam2()
first_exam.writing_grade = 100
first_exam.science_grade = 95
print('first_exam.writing_grade', first_exam.writing_grade)
print('first_exam.science_grade', first_exam.science_grade)
   
second_exam = Exam2()
second_exam.writing_grade = 55
print('second_exam.writing_grade', second_exam.writing_grade, 'is right')
print('first_exam.writing_grade', first_exam.writing_grade, 'is wrong')
