# -*- coding: utf-8 -*-

from opaque import OpaqueClass
from better import BetterClass
import json

class ComplexClass(object):
    def __init__(self, id, name, opaque, better):
        self.id = id
        self.name = name
        self.opaque = opaque
        self.better = better
    def dict(self):
        '''
　　　　　　　ComplexClassのフィールドがオブジェクトの場合、__dict__では値がオブジェクトになるので
           値が辞書型になるように対応。 
        '''
        tmp = self.__dict__.copy()
        tmp['opaque'] = self.opaque.__dict__ # オブジェクト or __repr__の戻り値なので、辞書型の表現に変更
        tmp['better'] = self.better.__dict__ # オブジェクト or __repr__の戻り値なので、辞書型の表現に変更
        return tmp

if __name__ == '__main__':      
    obj1 = OpaqueClass(10, 20, "test taro")
    obj2 = BetterClass(10, 20)
    obj = ComplexClass(id=100, name="コンプレックス！", opaque=obj1, better=obj2)
    print '-------------------------------------------------------------------'
    print obj
    print '-------------------------------------------------------------------'
    print obj.__dict__
    print '-------------------------------------------------------------------'
    print obj.dict()
    print '-------------------------------------------------------------------'
    print json.dumps(obj.dict(), indent=4)
