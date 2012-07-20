"""
Design an algorithm that, given a list of n elements in an array, 
finds all the elements that appear more than n/3 times in the list.
 
Expected is O(n).

You are expected to use comparisons and achieve linear time. No 
hashing/excessive space/ and don't use standard linear time
deterministic selection algo
"""


"""
http://apps.topcoder.com/forums/?module=RevisionHistory&messageID=1464587

Here is the algorithm. Maintain up to two elements and a positive counter for 
each. Scan through the array. If the next element x is the same as either 
stored element, increment the counter for that stored element. 
Otherwise, if there are fewer than two stored elements, store x and set its 
counter to 1. In the third case, if there are two stored elements and x is
different from both, decrement the counter for each stored element, 
unstoring it if the counter would become zero (since we require 
the counter to be positive).

After the scan, any special element will be one of the stored elements. 
Then you just need to verify them.
"""
def findElements(seq):
    elem1 = None
    elem2 = None
    counter1 = 0
    counter2 = 0
    
    for item in seq:
        if item == elem1:
            counter1 += 1
        elif item == elem2:
            counter2 += 1
        elif counter1 == 0:
            elem1 = item
            counter1 = 1
        elif counter2 == 0:
            elem2 = item
            counter2 = 1
        else:
            counter1 -= 1
            if counter1 == 0:
                elem1 = None
            counter2 -= 1
            if counter2 == 0:
                elem2 = None
    
    nn = len(seq) / 3
    result = []
    counter = 0
    if elem1 != None:
        for item in seq:
            if item == elem1:
                counter += 1
        if counter > nn:
            result.append(elem1)

    counter = 0
    if elem2 != None:
        for item in seq:
            if item == elem2:
                counter += 1
        if counter > nn:
            result.append(elem2)
    
    return result


seq = [1, 2, 3, 1, 3, 7, 1, 1, 2, 2, 2]
print findElements(seq)