from collections import defaultdict

def group_anagrams(words):
    
    anagrams = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)


    return list(anagrams.values())