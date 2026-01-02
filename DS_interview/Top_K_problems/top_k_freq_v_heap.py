
from collections import Counter 
import heapq

def top_k_frequencies(nums, k):
    count = Counter(nums)

    return [item for item, freq in heapq.nlargest(k, count.items(), key = lambda x: x[1])]