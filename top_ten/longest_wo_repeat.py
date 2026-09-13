def longest_wo_repeat(s):

    seen = {}
    left = max_len = 0 

    for right, char in enumerate(s):
        if char in seen and left >= seen[char]:
            left = seen[char] + 1
        max_len = max(max_len, right - left + 1)

        seen[char] = right

    return max_len