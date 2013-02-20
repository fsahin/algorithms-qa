"""
An inversion in an array a[] is a pair of entries a[i] and a[j] such that i<j 
but a[i]>a[j]. Given an array, design a linearithmic algorithm to count the 
number of inversions.
"""

def merge(seq1, seq2):
    inversions = 0
    i = 0
    j = 0
    n1 = len(seq1)
    n2 = len(seq2)
    result = []
    
    while i != n1 and j != n2:
        if seq1[i] <= seq2[j]:
            result.append(seq1[i])
            i += 1
        else:
            inversions += (n1 - i)             
            result.append(seq2[j])
            j += 1
    
    result += seq1[i:]
    result += seq2[j:]
    
    return (result, inversions)

def MergeSortInv(seq):
    if len(seq) <= 1:
        return seq, 0
    
    middle = len(seq) / 2
    left, invl = MergeSortInv(seq[:middle])
    right, invr = MergeSortInv(seq[middle:])
    merged = merge(left, right)
    return merged[0], merged[1] + invl + invr
    
seq = [5, 1, 7, 8, -2, -3]
print MergeSortInv(seq)
