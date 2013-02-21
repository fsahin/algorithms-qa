"""
Given an unsorted Array find maximum value of A[j] - A[i] where j>i in O(n) time
"""
seq = [5, 2, 6, 1, 8, 2]


def findMaxDiff(seq):
    #A[j] - A[i] is maximuml, when A[i] is the minimum betweeb A[i] and A[j]
    n = len(seq)
    maxDiff = -9999999
    minNum = seq[0]
    for i in xrange(1, n):
        maxDiff = max(seq[i] - minNum, maxDiff)
        minNum = min(seq[i], minNum)
    return maxDiff


print findMaxDiff(seq)
