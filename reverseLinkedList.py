'''
Reverse a linked list
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printLinkedList(root):
    while root != None:
        print root.data
        root = root.next

def reverseLinkedList(root):
    """
    Simple iteration and reverse 
    Returns the root of the reversed list
    """
    prev = None

    while root != None:
        next = root.next
        root.next = prev
        prev = root
        root = next
    return prev


one = Node("1")
two = Node("2")
three = Node("3")

one.next = two
two.next = three

one = reverseLinkedList(one)
printLinkedList(one)

