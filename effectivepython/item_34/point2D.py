# -*- coding: utf-8 -*-

from common import Serializable
from common import Deserializable

class Point2D(Serializable):
    def __init__(self, x, y):
        super(Point2D, self).__init__(x, y)
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'Point2D(%d,%d)' % (self.x, self.y)

point = Point2D(10, 5000)
print('Ojbect:' , point)
print('Serialized:', point.serialize())

print('------------------------------------------------------')

class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super(BetterPoint2D, self).__init__(x, y)
        self.x = x
        self.y = y
        
    def __repr__(self):
        return 'BetterPoint2D(%d,%d)' % (self.x, self.y)

point = BetterPoint2D(10, 5000)
print('Before:' , point)
data = point.serialize()
print('Serialized:', data)
after = BetterPoint2D.deserialize(data)
print('After:' , after)


