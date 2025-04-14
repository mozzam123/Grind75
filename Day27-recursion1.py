""" 
Print numbers from 1 to n in order
eg. 1,2,3,4, 5
"""




def print_numbers(current, n):
    if current > n:
        return
    
    print(current)

    return print_numbers(current + 1, n)

print_numbers(1, 5)