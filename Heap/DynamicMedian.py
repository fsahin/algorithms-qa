"""
Dynamic median. Design medHeap data type that supports insert in logarithmic time, 
find-the-median in constant time, and remove-the-median in logarithmic time.
"""
from heapq import *


class Back(float):
    def __lt__(self, other):
        return not float.__le__(self, other)
    def __le__(self, other):
        return not float.__lt__(self, other)
    def __gt__(self, other):
        return not float.__ge__(self, other)
    def __ge__(self, other):
        return not float.__gt__(self, other)


class MedianHeap(object):
    def __init__(self):
        self.median = None
        self.left = []      #MaxHeap
        self.right = []     #MinHeap
    
    def getMedian(self):
        return self.median
            
    def push(self, elem):
        if self.median == None:
            self.median = elem
            return
        if elem < self.median:
            heappush(self.left, Back(elem))
        else:
            heappush(self.right, elem)            
        if len(self.left) - len(self.right) > 1:
            heappush(self.right, self.median)
            self.median = heappop(self.left)
        elif len(self.right) - len(self.left) > 0:
            heappush(self.left, Back(self.median))
            self.median = heappop(self.right)            
            
    def removeMedian(self):
        if self.median == None:
            return None
        result = self.median
        if len(self.left) > len(self.right):
            self.median = heappop(self.left)
        elif len(self.right) > len(self.left):
            self.median = heappop(self.right)
        elif len(self.left) == len(self.right) != 0:
            self.median = heappop(self.right)
        else:
            self.median = None
        return result
        
    
        
medHeap = MedianHeap()
medHeap.push(0)
medHeap.push(5)
medHeap.push(10)
medHeap.push(15)
medHeap.push(20)
medHeap.push(25)

print medHeap.getMedian()
print medHeap.left
print medHeap.right
print medHeap.removeMedian()
print medHeap.removeMedian()
print medHeap.removeMedian()
print medHeap.removeMedian()
print medHeap.removeMedian()
print medHeap.removeMedian()
print medHeap.removeMedian()
print medHeap.left
print medHeap.right
    
        
    
    
    
    
