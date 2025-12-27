


# Sliding Window - Longest Substring with K Unique Characters
# Time Complexity: O(n) - each character visited at most twice (right pointer and left pointer)
# Space Complexity: O(k) - hash map stores at most k unique characters

def longest_substring_k_unique(s, k):

    if k == 0 or not s:
        return 0
    
    left = 0
    max_length = 0
    char_count = {}

    for right in range(len(s)):

        char_count[s[right]] = char_count.get(s[right],0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        if len(char_count) == k:
            max_length = max(max_length, right - left + 1)

    return max_length