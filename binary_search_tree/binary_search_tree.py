import sys
sys.path.append('../queue_and_stack')
from queue import Queue
from stack import Stack

# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    # Need to traverse to find spot to insert
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    # `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    # Start from root and traverse the tree
    # We can stop at the first instance of a value
    # We know it's not found if we get to a node that doesn't have children
    while True:
      if target == self.value:
        return True
      elif target < self.value and self.left is None:
        return False
      elif target > self.value and self.right is None:
        return False
      else:
        self = self.right



  def get_max(self):
    # `get_max` returns the maximum value in the binary search tree.
    while self.right is not None:
      self = self.right
    return self.value


  def for_each(self, cb):
    # `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work.
    pass