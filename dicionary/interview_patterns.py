# Hash Map Interview Patterns
# Collection of common interview patterns using dictionaries
# See individual function comments for complexity analysis

from collections import defaultdict, Counter

# Pattern 1: Two Sum (using dict for O(1) lookup)
# Time: O(n), Space: O(n)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return None

# Pattern 2: Group anagrams
# Time: O(n * m log m) where n = words, m = avg word length
# Space: O(n * m)
def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())




# Pattern 3: First unique character
# Time: O(n), Space: O(1) - at most 26 unique chars for lowercase English
def first_unique(s):
    freq = Counter(s)
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
print(first_unique("leetcode"))  # 0