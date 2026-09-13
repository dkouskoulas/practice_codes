


def longest_single(s):

    max_count = 1
    count = 1 #streak counter

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count