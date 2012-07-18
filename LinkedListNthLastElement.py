"""
Implement an algorithm to find the nth last element of a singly linked list
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def findNthLastElement(head, n):
    if head == None or n < 1:
        return None
    
    p1 = head
    p2 = head
    for i in range(n):
        if p2 == None:
            return None
        p2 = p2.next
    
    while p2 != None:
        p2 = p2.next
        p1 = p1.next
        
    return p1.data
    


ten = Node(10)    
nine = Node(9, ten)
eight = Node(8, nine)
seven = Node(7, eight)
six = Node(6, seven)
five = Node(5, six)
four = Node(4, five)
three = Node(3, four)
two = Node(2, three)
one = Node(1, two)

print findNthLastElement(one, 10) # Should return 1
print findNthLastElement(nine, 3) # Should return None