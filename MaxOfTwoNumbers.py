"""
Write a method which finds the maximum of two numbers. You should not use
if-else or any other comparison operators 
"""

def getMax(a, b):
    c = a- b
    k = (c >> 31) & 01
    max = a - (k * c)
    return max


print max(10, -20)