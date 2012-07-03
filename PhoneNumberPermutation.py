"""
For any phone number, the program should print out all the possible strings 
it represents. For example 2 can be replaced by 
'a' or 'b' or 'c', 3 by 'd' 'e' 'f' etc. 

"""
d = { 
    '0':"0",
    '1':"1",
    '2': "ABC",
    '3': "DEF",
    '4': "GHI",
    '5': "JKL",
    '6': "MNO",
    '7': "PQRS",
    '8': "TUV",
    '9': "WXYZ",
}

def permutatePhoneNum(number):
    '''
    Assuming that you simply output the value itself for 1 and 0,
    '''
    result = []
    if len(number) == 1:
        return [i for i in d[number]]

    restPerm = permutatePhoneNum(number[1:])
    for chr in d[number[0]]:
        for rest in restPerm:
            result.append(chr + rest)
    return result


print permutatePhoneNum("0704")