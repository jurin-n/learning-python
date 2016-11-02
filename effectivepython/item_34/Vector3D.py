# -*- coding: utf-8 -*-
from common import RegisteredSerializable, deserialize

class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super(Vector3D, self).__init__(x, y, z)
        self.x, self.y, self.z = x, y, z

print('[DEBUG]Vector3D test start')
v3 = Vector3D(500, -3, 800000)
print('Before:', v3)
data = v3.serialize()
print('Serialized:', data)
print('After:', deserialize(data))
print('[DEBUG]Vector3D test end')