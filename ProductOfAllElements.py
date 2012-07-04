'''
There is an array A[N] of N integers. You have to compose an array B[N] such 
that Output[i] will be equal to the product of all the elements of
A[] except A[i].

Example:
INPUT:[4, 3, 2, 1, 2]
OUTPUT:[12, 16, 24, 48, 24]

Solve it without the division operator and in O(n).

'''

def productOfAllElements(arr):
    n = len(arr)
    result = [1 for i in range(n)]

    p = 1
    for i in range(0, n):
        result[i] *= p
        p *= arr[i]
    
    p = 1
    for i in range(n-1, -1, -1):
        result[i] *= p
        p *= arr[i]
    
    return result
         
arr = [4, 3, 2, 1, 2]
print productOfAllElements(arr)