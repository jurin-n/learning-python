# -*- coding: utf-8 -*-
from functools import wraps

def trace(name):
    def _trace(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print('%s(%r,%r) -> %r with %s' % 
                  (func.__name__, args, kwargs, result, name))
            return result
        return wrapper
    return _trace

@trace('test-name123')
def something(n):
    print('n=',n)
    return n*n
    
something(1000)