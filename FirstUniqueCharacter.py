'''
Find the first unique character in a string containing only english characters
[a-z]
'''

import sys
def firstUnique(str):
    chars = []
    for i in range(26):
        chars.append([0, 0]) #First one is the position, second one is count
      
    for i, c in enumerate(str):
        val = ord(c) - ord('a')
        if chars[val][1] == 0:
            chars[val][0] = i
        chars[val][1] += 1
    
    minChr = sys.maxint
    found = False
    for tup in chars:
        if tup[1] == 1 and tup[0] < minChr:
            minChr = tup[0]
            found = True
    
    if found:
        return str[minChr] 
    else:   
        return None
    

str = "ffacssad"
print firstUnique(str)
