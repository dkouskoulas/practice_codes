# Recursion - Factorial
# Time Complexity: O(n) - n recursive calls
# Space Complexity: O(n) - call stack depth


def factorial(n):

    if n== 0 or n==1:
        return 1
    return n*factorial(n-1)