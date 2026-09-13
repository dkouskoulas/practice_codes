


def RLE(s):

    count = 1 
    result = ''

    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            result += str(count) + s[i-1]
            count = 1 

    result += str(count) + s[-1]
    return result\