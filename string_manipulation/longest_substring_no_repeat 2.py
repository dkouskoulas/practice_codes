# Question:
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3 (The answer is "abc", with the length of 3)

# Example 2:
# Input: s = "bbbbb"
# Output: 1 (The answer is "b", with the length of 1)

# Example 3:
# Input: s = "pwwkew"
# Output: 3 (The answer is "wke", with the length of 3)


# Approach 1: Sliding Window with Hash Map (Optimal)
# Time: O(n), Space: O(min(n, m)) where m is charset size
def lengthOfLongestSubstring(s):
    """
    Uses sliding window technique with a hash map to track character positions.
    When a duplicate is found, move left pointer to skip the duplicate.
    """
    char_index = {}  # Maps character to its most recent index
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If char is already in window, move left pointer
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        # Update the character's position
        char_index[char] = right
        
        # Calculate current window length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Approach 2: Sliding Window with Set
# Time: O(2n) = O(n), Space: O(min(n, m))
def lengthOfLongestSubstring_v2(s):
    """
    Uses a set to track characters in current window.
    Shrinks window from left when duplicate is found.
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Remove characters from left until no duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Approach 3: Returns the actual substring (not just length)
def longestSubstringNoRepeat(s):
    """
    Returns the actual longest substring without repeating characters.
    """
    char_index = {}
    left = 0
    max_length = 0
    start_index = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        
        # Update max_length and track starting position
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left
    
    return s[start_index:start_index + max_length]


# Test cases
if __name__ == "__main__":
    test_cases = [
        "abcabcbb",      # Expected: 3 ("abc")
        "bbbbb",         # Expected: 1 ("b")
        "pwwkew",        # Expected: 3 ("wke")
        "",              # Expected: 0
        "au",            # Expected: 2 ("au")
        "dvdf",          # Expected: 3 ("vdf")
        "abcdefg",       # Expected: 7 ("abcdefg")
    ]
    
    print("Testing lengthOfLongestSubstring:")
    for s in test_cases:
        result = lengthOfLongestSubstring(s)
        actual_substring = longestSubstringNoRepeat(s)
        print(f"Input: '{s}' -> Length: {result}, Substring: '{actual_substring}'")
