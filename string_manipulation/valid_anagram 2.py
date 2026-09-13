# Question:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True


# Alternative using Counter
from collections import Counter

def is_anagram_v2(s, t):
    return Counter(s) == Counter(t)
