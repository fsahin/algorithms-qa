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
    pass
    
    



faruk = Node("faruk")
emre = Node("emre")
sahin = Node("sahin")

faruk.next = emre
emre.next = sahin

printLinkedList(faruk)

