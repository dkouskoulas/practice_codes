# Recursion - Power (Naive)
# Time Complexity: O(exp) - exp recursive calls
# Space Complexity: O(exp) - call stack depth

def power(base, exp):

    if exp == 0:
        return 1
    
    return base*power(base,exp -1)