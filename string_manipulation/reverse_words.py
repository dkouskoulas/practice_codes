# Question:
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

def reverse_words(s):
    return ' '.join(s.split()[::-1])


# Without using split (more interview-friendly)
def reverse_words_v2(s):
    # Remove leading/trailing spaces and reduce multiple spaces
    words = []
    word = []
    
    for i, char in enumerate(s):
        if char != ' ':
            word.append(char)
        elif word:
            words.append(''.join(word))
            word = []
    
    if word:
        words.append(''.join(word))
    
    return ' '.join(words[::-1])
