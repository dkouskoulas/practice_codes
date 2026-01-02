

def is_palindrome(s):

    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return 'not palindrome'
        left += 1
        right -= 1

    return 'is palindrome'