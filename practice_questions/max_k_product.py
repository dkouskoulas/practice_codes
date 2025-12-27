

import heapq 
from math import prod

def max_product_k(arr, k):
    max_prod = float('-inf')
    
    largest = heapq.nlargest(k, arr)
    smallest = heapq.nsmallest(k, arr)

    for i in range(0, k + 1, 2):
        combo = smallest[:i] + largest[i:k]
        max_prod = max(max_prod, prod(combo))
    
    return max_prod