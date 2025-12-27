# Recursion - Sum Array Elements
# Time Complexity: O(n) - n recursive calls
# Space Complexity: O(n) - call stack depth


def array_sum(arr):

    if not arr:
        return 0 
    
    return arr[0] + array_sum(arr[1:])

