# -*- coding: utf-8 -*-

class LazyDB(object):
    def __init__(self):
        self.exists = 5
    
    def __getattr__(self, name):
        print('Called LazyDB.__getattr__(%s)' % name)
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value

data = LazyDB()
print('Before:', data.__dict__)
print('foo:   ', data.foo)
print('After: ', data.__dict__)

class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called LoggingLazyDB.__getattr__(%s)' % name)
        return super(self.__class__, self).__getattr__(name)

data = LoggingLazyDB()
print('exists:', data.exists)
print('foo:   ', data.foo)
print('foo:   ', data.foo)
