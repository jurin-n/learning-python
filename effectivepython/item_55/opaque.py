# -*- coding: utf-8 -*-
import json

class OpaqueClass(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	# def __repr__(self):
	# 	return self.__dict__
	
if __name__ == '__main__':
    obj = OpaqueClass(10, 20, "test taro")

    print obj
    print obj.__dict__
    print json.dumps(obj.__dict__)
