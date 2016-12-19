# -*- coding: utf-8 -*-
#
# __getattr__試す
#

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

#
# __getattribute__試す
#
class ValidatingDB(object):
    def __init__(self):
        self.exists = 5
    
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            # return super(self.__class__, self).__getattribute__(name)
            return self.__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

class ValidatingDB2(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            #return super().__getattribute__(name) # don't work on python 2.7.
            return object.__getattribute__(self, name)
        except AttributeError:
            print('AttributeError')
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

print('[INFO]dump ValidatingDB instance attr')
data = ValidatingDB2()
print('exits:', data.exists)
print('foo:  ', data.foo)
print('foo:  ', data.foo)
