"""
Given a linked list, pairwise swap elements. So,
1->2->3->4->5
becomes
2->1->4->3->5
"""
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printLinkedList(root):
    while root != None:
        print root.data, 
        root = root.next
    print

def pairwiseSwap(head):    
    prev = None
    temp = head

    while temp != None and temp.next != None:
        first = temp
        second = first.next
        if prev != None:
            prev.next = second
        else:
            head = second
        first.next = second.next
        second.next = first
        prev = first
        temp = first.next
    
    return head


one = Node("1")
two = Node("2")
three = Node("3")
four = Node("4")
five = Node("5")

one.next = two
two.next = three
three.next = four
four.next = five

printLinkedList(one)
one = pairwiseSwap(one)
printLinkedList(one)
