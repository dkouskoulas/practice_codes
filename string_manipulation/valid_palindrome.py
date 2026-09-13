# Question:
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters
# and ignoring cases.

def is_palindrome(s):

    left, right = 0, len(s) - 1

    while left < right:
        s_left = s[left]
        s_right = s[right]
        if s_left.isalnum() and s_right.isalnum():
            if s_left.lower() == s_right.lower():
                left += 1
                right -= 1
            else:
                return False
        elif not s_left.isalnum():
            left += 1
        elif not s_right.isalnum():
            right -= 1
        else:  
            left += 1
            right -= 1

    
    return True
