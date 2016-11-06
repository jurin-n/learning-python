# -*- coding: utf-8 -*-
import json
from mixins import ToDictMixin
from pprint import pprint

class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(100,
                  left=BinaryTree(800,right=BinaryTree(9)),
                  right=BinaryTree(900,left=BinaryTree(11))
                  )

print('[DEBUG] dump dict')
pprint(tree.to_dict())
print('')
print('[DEBUG] dump json from dict')
print(json.dumps(tree.to_dict(),indent=4))