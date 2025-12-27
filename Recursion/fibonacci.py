# Recursion - Fibonacci (Naive)
# Time Complexity: O(2^n) - exponential due to repeated calculations
# Space Complexity: O(n) - call stack depth (max depth = n)


def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)