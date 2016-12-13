# -*- coding: utf-8 -*-

def complex_func(a, b, c):
    import pdb;pdb.set_trace() #デバッガ設定
    a = a + 1
    b = b + 2
    c = c + 3
    return a + b + c

result = complex_func(3, 4, 5)

print('result = ' + str(result))