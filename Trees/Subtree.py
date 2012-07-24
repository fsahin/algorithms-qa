"""
You have two very large binary trees: T1, with millions of nodes,  and T2, 
with hundreds of nodes Create an algorithm to decide if T2 is a subtree of T1
"""

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def isSubTree(tree1, tree2):
    if tree1 == None:
        return False
    
    if tree1.data == tree2.data:
        if matchTree(tree1, tree2):
            return True

    return isSubTree(tree1.left, tree2) or \
            isSubTree(tree1.right, tree2) 

def matchTree(tree1, tree2):
    if tree2 == None:
        return True
    elif tree1 == None:
        return False

    if tree1.data != tree2.data:
        return False

    return matchTree(tree1.left, tree2.left) and \
        matchTree(tree1.right, tree2.right)
        


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
    
print isSubTree(a, b)
print isSubTree(b, c)