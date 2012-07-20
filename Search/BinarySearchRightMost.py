"""
Write a search method that returns the rightmost index of the given element
in a sorted array
"""

def binarySearchR(seq, x):
    return binSearchRight(seq, 0, len(seq) - 1, x)
    
def binSearchRight(seq, left, right, x):
    mid = (left + right) / 2
    if seq[mid] == x:
        if mid == len(seq) - 1:
            return mid
        elif seq[mid + 1] == x:
            return binSearchRight(seq, mid + 1, right, x)
        else:
            return mid
    elif left == right:
        return None
    elif x > seq[mid]:
        return binSearchRight(seq, mid + 1, right, x)
    else:
        return binSearchRight(seq, left, mid - 1, x)



seq = [-2, -1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3]
print binarySearchR(seq, -1)
print binarySearchR(seq, 3)