"""
Write a program to sort a stack in ascending order
"""

def sortStack(stack):
    """
    Use a helper stack to sort the original stack, 
    Uses a python list as a stack, 
    Complexity = O(N^2)
    """
    dest = []
    while len(stack) != 0:
        tmp = stack.pop()
        while (len(dest) != 0 and dest[-1] > tmp):
            stack.append(dest.pop())
        dest.append(tmp)
            
    return dest
    

stack = [6, 4, 7, 9, 0, -1]
print sortStack(stack)
    


