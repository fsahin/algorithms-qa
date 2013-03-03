"""
Check if a binary tree is a BST. Given a binary tree where each Node contains a
key, determine whether it is a binary search tree.
Use extra space proportional to the height of the tree.
"""

import sys

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isBST(root):
    """
    Check if the tree is in sorted order in in-order traversal.
    
    If the node has a left child, push the node again and then its left child 
    since the node has to be visited again after its left subtree.
    """
    s = []
    s.append((root, False)) #Not visited
    prev = -sys.maxint
    
    while len(s) != 0:
        item = s.pop()
        node = item[0]
        if item[1] == True:
            print node.data,
            if node.data < prev:
                return False
            prev = node.data
            if not node.right is None:
                s.append((node.right, False))            
        else:
            if node.left != None:
                s.append((node, True))  #Visited
                s.append((node.left, False))
            else:
                print node.data
                if node.data < prev:
                    return False
                prev = node.data
                if not node.right is None:
                    s.append((node.right, False))
    
    return True
    
    
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)


three.right = four
three.left = two
two.left = one
four.right = five
five.left = six


print isBST(three)

        
        
