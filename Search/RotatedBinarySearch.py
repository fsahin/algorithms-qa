""" Find an item in a rotated sorted list on O(logn) time"""

def search(seq, x):
    return searchRotList(seq, x, 0, len(seq)-1)

def searchRotList(seq, x, left, right):
    while (left <= right):
        mid = (left + right) / 2
        if x == seq[mid]:
            return mid
        elif seq[left] <= seq[mid]: #If left part is ordered
            if x > seq[mid]:
                left = mid + 1
            elif x >= seq[left]:
                right = mid -1
            else:
                left = mid + 1
        elif x < seq[mid]: #It means right part is ordered, so if x < seq[mid] its on the left side
            right = mid -1
        elif x <= seq[right]: #
            left = mid + 1
        else:
            right = mid -1
        
    return None


seq = [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
print search(seq, 9)
    