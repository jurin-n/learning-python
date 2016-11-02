# -*- coding: utf-8 -*-
import json

class Serializable(object):
    def __init__(self, *args):
        self.args = args
    
    def serialize(self):
        return json.dumps({'args':self.args})

class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args,
        })

    def __repr__(self):
        return '%s(%s)' % (
            self.__class__.__name__,
            ', '.join(str(x) for x in self.args))
    
registry = {}
    
def register_class(target_class):
    registry[target_class.__name__] = target_class
    
def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print('[DEBUG]Meta.__new__ start')
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        print('[DEBUG]Meta.__new__ end')
        return cls

class RegisteredSerializable(BetterSerializable):
    # Python2とPython3でMetaクラスの書き方違うので注意
    print('[DEBUG]RegisteredSerializable.__metaclass__ start')
    __metaclass__=Meta
    print('[DEBUG]RegisteredSerializable.__metaclass__ end')
