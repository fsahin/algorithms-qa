"""
The diameter of a tree is the number of nodes on the longest path between two 
leaves in the tree. The diagram below shows a tree with diameter nine, the 
leaves that form the ends of a longest path are shaded (note that there is more 
than one path in each tree of length nine, but no path longer than nine nodes).  

In particular, note that the diameter of a tree T is the largest of 
the following quantities:

the diameter of T's left subtree
the diameter of T's right subtree
the longest path between leaves that goes through the root of T
 
Given the root node of a binary tree, return the diameter of the tree
"""
class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def diameter(node):
    if node is None:
        return 0
    return max(diameter(node.left), diameter(node.right), distanceLR(node))

def distanceLR(node):
    return height(node.left) + height(node.right) + 1

def height(node):
    if node == None:
        return 0
    return 1 + max(height(node.left), height(node.right))

"""
             a
           /   \
          b     c
        /  \   /  \
       d    e f    g
     /  \
    h    i
"""
h = BinaryTreeNode("h")
i = BinaryTreeNode("i")
d = BinaryTreeNode("d", h, i)
e = BinaryTreeNode("e")
f = BinaryTreeNode("f")
g = BinaryTreeNode("g")
b = BinaryTreeNode("b", d, e)
c = BinaryTreeNode("c", f, g)
a = BinaryTreeNode("a", b, c)

print diameter(a)


