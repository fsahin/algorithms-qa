"""
Given a sequence of numbers, find the maximum sum of a contiguous subsequence of
those numbers.
"""

def maximumSubsequenceSum(seq):
    """
    Return 0, 0, 0 if the list has only positive numbers or the list is empty
    """
    n = len(seq)
    curSum = 0
    maxSum = 0
    maxStart = 0
    maxEnd = 0
    curStart = 0
    curEnd = 0
    for i in range(n):
        curSum = curSum + seq[i]
        if curSum < 0:
            curSum = 0
            curStart = i + 1
        else:
            curEnd = i
        
        if curSum > maxSum:
            maxSum = curSum
            maxStart = curStart
            maxEnd = i
    
    return maxStart, maxEnd, maxSum
        

seq = [-6, 2, 1, 12, -14, 13, 45]
seq2 = [0, 0, 0]

print maximumSubsequenceSum(seq)
print maximumSubsequenceSum(seq2)
            
        
        
