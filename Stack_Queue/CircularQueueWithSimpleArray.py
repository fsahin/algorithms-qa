"""
Implement a circular queue of integers of user-specified size using a simple 
array. Provide routines to initialize(), enqueue() and dequeue() the queue. 
Make it thread safe.
"""
from threading import Lock
class CircularQueue(object):
    """
    Always keep one slot open to differentiate between full/empty buffer
    """
    def __init__(self, size):
        self.size = size + 1
        self.q = [0 for i in range(size + 1)]
        self.head = 0
        self.tail = 0
        self.lock = Lock()

    def initialize(self):
        self.lock.acquire()
        self.head = 0
        self.tail = 0
        self.lock.release()
    
    def enqueue(self, item):
        self.lock.acquire()
        temp = (self.tail + 1 ) % self.size
        if temp == self.head:
            self.lock.release()
            return False
        self.q[self.tail] = item
        self.tail = temp
        self.lock.release()
        return True
    
    def dequeue(self):
        self.lock.acquire()
        if self.head == self.tail:
            lock.release()
            raise Exception("No item in the queue")
        temp = self.q[self.head]
        self.head = (self.head + 1) % self.size
        self.lock.release()
        return temp
        
cq = CircularQueue(3)

print cq.enqueue(10)
print cq.enqueue(20)
print cq.enqueue(30)
print cq.enqueue(40)
print cq.dequeue()
print cq.dequeue()
print cq.dequeue()
