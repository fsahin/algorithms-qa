def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        midval = a[mid]
        if midval < x:
            lo = mid + 1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1


seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print binary_search(seq, 5)
