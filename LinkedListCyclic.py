"""
Write a function that takes a pointer to the head of a list and determines 
whether the list is cyclic or acyclic. Your function should return false if 
the list is acyclic and true if it is cyclic. 
You may not modify the list in any way.
"""
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
def isCyclic(head):
    if head.next == None:
        return False
    fast = head.next.next
    slow = head.next
    
    while 1:
        if fast == None or fast.next == None:
            return False
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
        

three = Node("3")
two = Node("2", three)
one = Node("1",two)

print isCyclic(one)

three.next = one
print isCyclic(one)

one.next = one
print isCyclic(one)