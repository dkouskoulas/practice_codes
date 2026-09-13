

def is_anagram(s1, s2):

    chars_s1 = {}
    chars_s2 = {}

    for s in s1:
        chars_s1[s] = chars_s1.get(s,0) + 1
        
    for s in s2:
        chars_s2[s] = chars_s2.get(s,0) + 1

    return chars_s1 == chars_s2