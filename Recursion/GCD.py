# Recursion - Greatest Common Divisor (Euclidean Algorithm)
# Time Complexity: O(log min(a, b)) - reduces problem size logarithmically
# Space Complexity: O(log min(a, b)) - call stack depth


def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)