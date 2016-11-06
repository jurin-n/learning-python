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
                  left=BinaryTree(800, right=BinaryTree(9)),
                  right=BinaryTree(900, left=BinaryTree(11))
                  )

print('[DEBUG] dump dict')
pprint(tree.to_dict())
print('')
print('[DEBUG] dump json from dict')
print(json.dumps(tree.to_dict(), indent=4))

class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super(BinaryTreeWithParent, self).__init__(value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key, value):
        if(isinstance(value, BinaryTreeWithParent) and key == 'parent'):
            return value.value 
        else:
            return super(BinaryTreeWithParent, self)._traverse(key, value)
        
root = BinaryTreeWithParent(100)
root.left = BinaryTreeWithParent(800, parent=root)
root.left.right = BinaryTreeWithParent(900, parent=root.left)
                                
print('[DEBUG] dump dict')
pprint(root.to_dict())
print('')
print('[DEBUG] dump json from dict')
print(json.dumps(root.to_dict(), indent=4))
