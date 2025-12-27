




# Two Pointers - Check if String is Palindrome
# Time Complexity: O(n) - check half the string
# Space Complexity: O(1) - only uses constant extra space

def is_palindrome(s):

    left, right = 0, len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left +=1 
        right -=1
    return True