"""
Write a method that returns all subsets of a set.
"""

def getSubSets(seq):
    if len(seq) == 0:
        return [[]]
    else:
        subSets = getSubSets(seq[1:])
        newSubs = []
        for sub in subSets:
            newSubs.append(sub + [seq[0]])
        subSets.extend(newSubs)
        return subSets
            
seq = [1, 2, 3]
print getSubSets(seq)