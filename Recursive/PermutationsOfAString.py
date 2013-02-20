"""
Implement a routine that prints all possible orderings of the characters in a 
string. In other words, print all permutations that use all the characters 
from the original string. For example, given the string 'hat', your function 
should print the strings 'tha', 'aht', 'tah', 'ath', 'hta', and 'hat. 
Treat each character in the input string as a distinct character, even if it 
is repeated. Given the string 'aaa', your routine should print 'aaa' six times. 
You may print the permutations in any order you choose.

Also get combinations..
"""

def getPermutations(s):
    if len(s) == 1:
        return [s]
    else:
        perms = getPermutations(s[1:])
        p = []
        for perm in perms:
            for i in range(len(perm) + 1):
                p.append(perm[0:i] + s[0] + perm[i:])
        return p

def getCombinations(s):
    if len(s) == 0:
        return [['']]
    else:
        combs = getCombinations(s[1:])
        r = combs[:]
        for comb in combs:
            r.append([s[0] + comb[0]])
        return r

s = "abcd"
print getPermutations(s)
print getCombinations(s)

