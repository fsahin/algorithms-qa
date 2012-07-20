"""
Implement a routine that prints all possible orderings of the characters in a 
string. In other words, print all permutations that use all the characters 
from the original string. For example, given the string 'hat', your function 
should print the strings 'tha', 'aht', 'tah', 'ath', 'hta', and 'hat. 
Treat each character in the input string as a distinct character, even if it 
is repeated. Given the string 'aaa', your routine should print 'aaa' six times. 
You may print the permutations in any order you choose.
"""


def getPermutations(str):
    if len(str) == 1:
        return [str]
    else:
        perms = getPermutations(str[1:])
        p = []
        for perm in perms:
            for i in range(len(perm) + 1):
                p.append(perm[0:i] + str[0] + perm[i:])
        return p
        

str = "abcd"
print getPermutations(str)

