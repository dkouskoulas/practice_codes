from collections import Counter

import heapq

#nlogk
def topKFrequent(nums, k):
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key = freq.get)


#nlogn
def topKFrequency_b(nums,k):
    freq_dict = Counter(nums)
    frequencies_sorted = sorted(freq_dict.items(), key = lambda x: x[1])
    top_k = frequencies_sorted[-k:]
    return top_k


def topKFrequency_c(nums, k):
    freq = Counter(nums)
    return sorted(freq, key = freq.get)[-k:]

