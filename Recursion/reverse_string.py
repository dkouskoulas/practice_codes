# Recursion - Reverse String
# Time Complexity: O(n) - n recursive calls
# Space Complexity: O(n) - call stack depth + string concatenation



def reverse_string(s):

    if len(s) <= 1:
        return s 
    
    return s[-1] + reverse_string(s[:-1])