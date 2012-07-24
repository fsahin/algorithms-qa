def quickSort(seq):
    if len(seq) == 0:
        return seq
    
    pivot = seq[0]
    lesser = quickSort([x for x in seq[1:] if x < pivot])
    greater = quickSort([x for x in seq[1:] if x >= pivot])
    return lesser + [pivot] + greater

seq = [5, 8, -2, 3, 12, -23, -12]
print quickSort(seq)