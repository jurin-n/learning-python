# -*- coding: utf-8 -*-

from common import BetterSerializable, register_class, deserialize

class EvenBetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super(EvenBetterPoint2D, self).__init__(x, y)
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'EvenBetterPoint2D(%d,%d)' % (self.x, self.y)

register_class(EvenBetterPoint2D)

point = EvenBetterPoint2D(500, 3333)
print('Before:', point)
data = point.serialize()
print('Serialized:', data)
after = deserialize(data)
print('After:', after)
