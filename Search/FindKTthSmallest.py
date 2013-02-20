"""
Find the k th largest element in an array in lineer time
"""

def kLargestElement(seq, k):
    if k > len(seq):
        return None
    pivot = seq[-1]
    less = [x for x in seq[:-1] if x < pivot]
    greater = [x for x in seq[:-1] if x >= pivot]
    if len(greater) + 1 == k:
        return pivot
    elif k <= len(greater):
        return kLargestElement(greater, k)
    else:
        return kLargestElement(less, k - len(greater) - 1)
    

seq = [1, 8, 6, 5, 7, 2, 4, 3, 9, 10, 10, 9]
print kLargestElement(seq, 12)

