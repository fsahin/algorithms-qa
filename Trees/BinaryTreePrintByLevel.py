"""
Given a binary tree, print out the data level by level starting from the top
"""

from collections import deque
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def printLevel(node):
    """ Breadth-first traversal, print out the data by level """
    level = 0
    lastPrintedLevel = 0
    visit = deque([])
    visit.append((node, level))
    while len(visit) != 0:
        item = visit.popleft()
        if item[1] != lastPrintedLevel:  #New line for a new level
            lastPrintedLevel +=1
            print
        print item[0].data,
        if item[0].left != None:
            visit.append((item[0].left, item[1] + 1))
        if item[0].right != None: 
            visit.append((item[0].right, item[1] + 1))


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

printLevel(a)