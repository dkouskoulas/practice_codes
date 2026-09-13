# Question:
# Given two strings needle and haystack, return the index of the first occurrence 
# of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    if not needle:
        return 0
    
    if len(needle) > len(haystack):
        return -1
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1


# Alternative: Using two pointers (more efficient for large inputs)
def strStr_v2(haystack, needle):
    if not needle:
        return 0
    
    n, m = len(haystack), len(needle)
    
    for i in range(n - m + 1):
        j = 0
        while j < m and haystack[i + j] == needle[j]:
            j += 1
        if j == m:
            return i
    
    return -1
