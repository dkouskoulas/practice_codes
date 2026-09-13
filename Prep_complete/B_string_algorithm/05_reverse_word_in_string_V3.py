

def revesre_words_inplace(s):

    chars = list(s)

    #define a helper function
    def reverse(l, r):
        while l < r:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1 
            r -= 1 

    #step 1: reversele string
    reverse(0, len(chars) - 1)

    #step 2: revesre each word
    start = 0 
    for i in range(len(chars) + 1):

        if i == len(chars) or chars[i] == ' ':
            reverse(start, i - 1)
            start = i + 1
            
    return "".join(chars)
