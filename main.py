# def printNumbers(n):
#     if n == 0:
#         return
#     print(n)
#     printNumbers(n-1)


# printNumbers(3)




def reverse_string(s):
    s = list(s)
    reverse_str = []
    length = len(s) - 1

    if len(s) == 0:
        return
    print(s[length])
    length -= 1
    reverse_str()
    

reverse_string("hello")