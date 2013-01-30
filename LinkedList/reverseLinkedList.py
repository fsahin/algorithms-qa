'''
Reverse a linked list
'''

class Node:
    def __init__(self, data=None, nextt=None):
        self.data = data
        self.next = nextt

def printLinkedList(root):
    while root != None:
        print root.data,
        root = root.next
    print

def reverseLinkedList(head):
    """
    Simple iteration and reverse 
    Returns the root of the reversed list
    """
    prev = None
    while head != None:
        nextt = head.next
        head.next = prev
        prev = head
        head = nextt
    return prev

def reverseList(head, prev):
    """
    Recursively reverse a linked list
    """
    if head.next == None:
        head.next = prev
        return head
    else:
        newhead = reverseList(head.next, head)
        head.next = prev
        return newhead


one = Node("1")
two = Node("2")
three = Node("3")

one.next = two
two.next = three

printLinkedList(one)
reverse = reverseLinkedList(one)
printLinkedList(reverse)

