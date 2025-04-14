def print_numbers(current, n):
    if current > n:
        return
    
    print(current)

    return print_numbers(current + 1, n)

print_numbers(1, 5)