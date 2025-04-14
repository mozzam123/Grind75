"""
print number n in reverse
eg. 5,4,3,2,1
"""



def reverse_number(n):
    if n == 0:
        return
    print(n)

    return reverse_number(n-1)


reverse_number(5)