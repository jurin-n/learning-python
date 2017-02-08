# -*- coding: utf-8 -*-
"""
 @propertyの動作を確認するためのサンプルコード。
"""
class FixedResistance(object):
    def __init__(self, ohms):
        self._ohms = ohms
        self._voltage = 0
        self._current = 0
    
    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, value):
        self._check_attr('_ohms')
        self._ohms = value

    def _check_attr(self, name):
        if hasattr(self, name):
            raise AttributeError("Can't set attribute " + name)
        
r4 = FixedResistance(1e3)
print('[DEBUG]---------------------------------------')
print('r4.ohms=%5r' % r4.ohms)
print('[DEBUG]---------------------------------------')
r4.ohms = 2e3
print('r4.ohms=%5r' % r4.ohms)
