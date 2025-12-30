# Hash Map - Group Anagrams
# Time Complexity: O(n * m log m) where n = number of words, m = average word length (sorting each word)
# Space Complexity: O(n * m) - stores all words in hash map


word_a = 'hello'
word_b = 'helol'
word_c = 'abc'
word_d = 'cba'

word_list = [word_a, word_b, word_c, word_d]

from collections import defaultdict

my_dict = defaultdict(list)



for word in word_list:
    key = ''.join(sorted(word))
    my_dict[key].append(word)

print(my_dict)