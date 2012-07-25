class Node(object):
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

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
    
def insertNode(root, node):
    if node.key < root.key:
        if root.left == None:
            root.left = node
        else:
            insertNode(root.left, node)
    else:
        if root.right == None:
            root.right = node
        else:
            insertNode(root.right, node)

def search_binary_tree(node, key):
    if node is None:
        return None  # key not found
    if key < node.key:
        return search_binary_tree(node.leftChild, key)
    elif key > node.key:
        return search_binary_tree(node.rightChild, key)
    else:  # key is equal to node key
        return node.data  # found key
    

one = Node(1, "one")
two = Node(2, "two")
three = Node(3, "three")
four = Node(4, "four")
five = Node(5, "five")

insertNode(three, two)
insertNode(three, one)
insertNode(three, four)
insertNode(three, five)

traverseBreadthFirst(three)