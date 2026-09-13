from collections import Counter

def checkInclusion(s1, s2):

    need = Counter(s1)
    k = len(s1)

    for i in range(len(s2) - k + 1):
        window = Counter(s2[i: i+k])
        if window == need:
            return True
        
    return False