# -*- coding: utf-8 -*-
import json

class BetterClass(object):	
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #def __repr__(self):
    #	return 'BetterClass(%d,%d)' % (self.x,self.y)
    	# return self.__dict__

if __name__ == '__main__':
    obj = BetterClass(10,20)

    print obj
    print obj.__dict__
    print json.dumps(obj.__dict__)