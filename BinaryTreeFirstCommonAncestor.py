"""
Given a Binary Tree ( Not a binary search tree), and values/data of two nodes, 
find the first common ancestor.

Solution from the book "Cracking the Coding Interview", Question 4.6

"""

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

TWO_NODES_FOUND = 2
ONE_NODE_FOUND = 1
NO_NODES_FOUND = 0

def covers(root, p, q):
    ret = NO_NODES_FOUND
    if root == None:
        return ret
    if (root == p):
        ret += 1
    if root == q:
        ret += 1
    if ret == TWO_NODES_FOUND:
        return ret
    
    ret += covers(root.left, p, q)
    if ret == TWO_NODES_FOUND:
        return ret
    return ret + covers(root.right, p ,q)

def commonAncestor(root, p, q):
    """
    For any node r,
    If p is on one side and q is on the other, r is the first common ancestor
    Else, the first common ancestor on on the left or the right side  
    """
    if q == p and (root.left == q or root.right == q):
        return root
    nodesFromLeft = covers(root.left, p, q)
    if nodesFromLeft == TWO_NODES_FOUND:
        if root.left == p or root.left == q:
            return root.left
        else:
            return commonAncestor(root.left, p, q)
    elif nodesFromLeft == ONE_NODE_FOUND:
        if root == p:
            return p
        elif root == q:
            return q
    
    nodesFromRight = covers(root.right, p, q)
    if nodesFromRight == TWO_NODES_FOUND:
        if root.right == p or root.right == q:
            return root.right
        else:
            return commonAncestor(root.right, p, q)
    elif nodesFromRight == ONE_NODE_FOUND:
        if root == p:
            return p
        elif root == q:
            return q
    
    if nodesFromLeft == ONE_NODE_FOUND and nodesFromRight == ONE_NODE_FOUND:
        return root
    else:
        return None


"""
             a
           /   \
          b     c
        /  \   /  \
       d    e f    g
     /  \
    h    i
"""
h = Node("h")
i = Node("i")
d = Node("d", h, i)
e = Node("e")
f = Node("f")
g = Node("g")
b = Node("b", d, e)
c = Node("c", f, g)
a = Node("a", b, c)

print commonAncestor(a, h, e).data # Should print b
print commonAncestor(a, i, g).data # Should print a
print commonAncestor(a, c, f).data # Should print c
print commonAncestor(a, g, g).data # Should print c