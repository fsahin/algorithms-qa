"""
Find largest 1 million numbers in 1 billion numbers.
Assume that the computer memory can hold all one billion numbers.
"""

def findTop(seq, start, stop, M):
    pivot = seq[start]
    smaller = [i for i in seq[start + 1:stop] if i < pivot]
    greater = [i for i in seq[start + 1:stop] if i >= pivot]
    seq = seq[:start] + smaller + [pivot] + greater + seq[stop:]
    if len(greater) + 1 == M :
        return seq[stop - M:]
    if M > len(greater):
        return findTop(seq, start, len(smaller), M - len(greater) - 1)
    else:
        return findTop(seq, start + len(smaller) + 1, stop, M)
        

def findTopM(seq, M):
    return findTop(seq, 0, len(seq), M)

seq = [1, 5, 8, 2, 9]
print findTopM(seq, 3) 
    
    
    
    
    
    
