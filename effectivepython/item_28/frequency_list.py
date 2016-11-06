# -*- coding: utf-8 -*-

class FrequencyList(list):
    def __init__(self, members):
        super(FrequencyList, self).__init__(members)
    
    def frequency(self):
        counts = {}
        for item in self:
            print('[DEBUG]frequency.item=', item)
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts


foo = FrequencyList(['a', 'b', 'c', 'd', 'a', 'a', 'c', 'e'])
print('length is', len(foo))
foo.pop()
print('After pop:', repr(foo))
print('Frequency:', foo.frequency())

