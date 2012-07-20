"""
Implement a queue using two stacks
"""
class Node(object):
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0
    
    def pop(self):
        if self.top == None:
            return None
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item
        
    def push(self, data):
        item = Node(data)
        item.next = self.top
        self.top = item
        self.size += 1
    
    def peek(self):
        if self.top == None:
            return None
        return self.top.data
    
    def isEmpty(self):
        if size == 0:
            return true
        return false

class Queue:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None
    
    def enqueue(self, data):
        if self.first == None:
            self.first = Node(data)
            self.last= self.first
        else:
            item = Node(data)
            self.last.next = item
            self.last = item
        self.size += 1
    
    def dequeue(self):
        if self.first == None:
            return None
        else:
            item = self.first
            self.first = self.first.next
            return item.data
    
class MyQueue:
    """Implement a queue using two stacks"""
    stack1 = Stack()
    stack2 = Stack()
    
    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        item = self.stack1.pop()
        while item!= None:
            self.stack2.push(item)
            item = self.stack1.pop()
        
        result = self.stack2.pop()
        
        item = self.stack2.pop()
        while item!= None:
            self.stack1.push(item)
            item = self.stack2.pop()
        
        return result
    
q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print q.dequeue()
print q.dequeue()
print q.dequeue()