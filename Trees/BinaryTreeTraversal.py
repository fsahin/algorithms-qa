class BinaryTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def traversePreOrder(root):
    """
    To traverse a non-empty binary tree in preorder, perform the following 
    operations recursively at each node, starting with the root node:
        1. Visit the root.
        2. Traverse the left subtree.
        3. Traverse the right subtree.
    """
    if root == None:
        return
    print root.data,
    traversePreOrder(root.left)
    traversePreOrder(root.right)
    
def traverseInOrder(root):
    """
    To traverse a non-empty binary tree in inorder (symmetric), perform 
    the following operations recursively at each node:
        1. Traverse the left subtree.
        2. Visit the root.
        3. Traverse the right subtree.
    """
    if root == None:
        return
    traverseInOrder(root.left)
    print root.data,
    traverseInOrder(root.right)
    
def traversePostOrder(root):
    """
    To traverse a non-empty binary tree in postorder, perform the 
    following operations recursively at each node:
        1. Traverse the left subtree.
        2. Traverse the right subtree.
        3. Visit the root.
    """
    if root == None:
        return
    traversePostOrder(root.left)
    traversePostOrder(root.right)
    print root.data,

from collections import deque
def traverseBreadthFirst(root):
    visit = deque([])
    visit.append(root)
    while len(visit) != 0:
        node = visit.popleft()
        print node.data, 
        if node.left != None:
            visit.append(node.left)
        if node.right != None:
            visit.append(node.right)
    


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

print "PreOrder Traversal:"
traversePreOrder(a)
print

print "InOrder Traversal:"
traverseInOrder(a)
print

print "Post Order Traversal:"
traversePostOrder(a)
print

print "Breadth First Traversal:"
traverseBreadthFirst(a)
print