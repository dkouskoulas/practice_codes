# Recursion - Climbing Stairs (Naive Fibonacci)
# Time Complexity: O(2^n) - exponential due to repeated calculations
# Space Complexity: O(n) - call stack depth



def climb_stairs(n):
    if n <= 1:
        return 1
    return climb_stairs(n-1) + climb_stairs(n-2)