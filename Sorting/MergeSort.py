def merge(seq1, seq2):
    i = 0
    j = 0
    n1 = len(seq1)
    n2 = len(seq2)
    result = []
    
    while i != n1 and j != n2:
        if seq1[i] < seq2[j]:
            result.append(seq1[i])
            i += 1
        else:
            result.append(seq2[j])
            j += 1
    
    result += seq1[i:]
    result += seq2[j:]
    
    return result


def MergeSortInv(seq):
    if len(seq) <= 1:
        return seq
    
    middle = len(seq) / 2
    left = MergeSortInv(seq[:middle])
    right = MergeSortInv(seq[middle:])
    return merge(left, right)
    


seq = [3, 7, 1, 9, -2, 4, 12, -45]
print MergeSortInv(seq)