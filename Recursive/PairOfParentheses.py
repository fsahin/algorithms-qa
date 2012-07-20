"""
Write a simple program to generate all the valid combinations 
of open/close parentheses for a given even number n. For n = 6:
((()))
(()())
(())()
()(())
()()()
"""

def printParanthesis(n):
    a = n / 2
    printP("", a, a)

def printP(str, l, r):
    if l == 0 and r == 0:
        print str

    if r > l:
        printP(str + ')', l, r - 1)
    
    if l > 0:
        printP(str + '(', l - 1, r)
         

printParanthesis(6)