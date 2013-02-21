"""
Given two sorted arrays a[] and b[], of sizes N1 and N2, respectively, design 
an algorithm to find the kth smallest key. The order of growth of the worst case 
running time of your algorithm should be logN, where N=N1+N2.
"""

def kthSmallest(seq1, seq2, k):
    i = 0
    j = 0
    n1 = len(seq1)
    n2 = len(seq2)
    x = 1
    if k > n1 + n2:
        return None
    
    while (i != n1 and j != n2):
        if (seq1[i] < seq2[j]):
            if x == k:
                return seq1[i]
            i += 1
        else:
            if x == k:
                return seq2[j]
            j += 1
        x += 1
    
    if i == n1:
        return seq2[j + k - x]
    elif j == n2:
        return seq1[i + k - x]
    return None

seq1 = [1, 3, 5, 7, 9, 11]
seq2 = [8, 10, 14, 18, 23, 45]
print kthLargest(seq1, seq2, 9)
