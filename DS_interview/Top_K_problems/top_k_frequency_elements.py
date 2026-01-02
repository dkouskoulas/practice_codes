

from collections import Counter

def top_k_freq(nums,k ):
    counts = Counter(nums)
    
    sorted_items = sorted(counts.items(), key = lambda x: x[1], reverse = True)

    return [item for item, freq in sorted_items[:k]]

