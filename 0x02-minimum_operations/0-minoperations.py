#!/usr/bin/python3
"""
Main file for testing
"""
def minOperations(n):
    if n <= 1:
        return 0  # No operations needed if n is 1 or less (we already have 1 'H')

    operations = 0
    # Try to factorize n starting from the smallest factor (2)
    i = 2
    while i * i <= n:
        # If i is a divisor of n
        while n % i == 0:
            operations += i  # Copy All (1 operation) + Paste (i-1 operations)
            n //= i
        i += 1
    
    # If n is still greater than 1, it means n itself is a prime number
    if n > 1:
        operations += n  # Copy All (1 operation) + Paste (n-1 operations)

    return operations
