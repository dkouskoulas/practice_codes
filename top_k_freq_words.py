from collections import defaultdict

def top_k_freq_words(words, k):
    if not words:
        return 0

    freq_dict = defaultdict(int)

    for word in words:
        freq_dict[word] += 1 

    words_list = [[key,val] for key, val in freq_dict.items()]

    words_list_sorted = sorted(words_list, key = lambda x: (-x[1],x[0]))

    just_words = [pair[0] for pair in words_list_sorted]
    result = just_words[:k]


    return result

if __name__ == "__main__":

    words = ["i", "banana", "banana", "i", "totalitarian", "cheese", "pizza", "pizza","pizza"]

