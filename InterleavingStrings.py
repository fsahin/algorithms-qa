"""
Given two strings, print all the interleaving of the two strings keeping the
order of the characters. If 'B' comes after 'A' in a string, it should also 
come after 'A' in the  joined string

Example:
AB and CD
ABCD
ACBD
ACDB
CABD
CADB
CDAB
"""

def interleaveStrings(str1, str2):
    interleave("", str1, str2)

def interleave(str, str1, str2):
    if len(str1) == 0 and len(str2) == 0:
        print str
        return
    
    if len(str1) != 0:
        interleave(str + str1[0], str1[1:], str2)
    
    if len(str2) != 0:
        interleave(str + str2[0], str1, str2[1:])

str1 = "AB"
str2 = "CD"

interleaveStrings(str1, str2)
