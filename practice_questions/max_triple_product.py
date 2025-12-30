# Heap - Maximum Product of Three Numbers
# Time Complexity: O(n) - heapq.nlargest/nsmallest are O(n) for small k
# Space Complexity: O(1) - only stores constant number of elements

import heapq 

def max_triple_prod(arr):


    a = heapq.nlargest(3,arr)
    b = heapq.nsmallest(2,arr)

    max_prod = max(a[0]*a[1]*a[2],b[0]*b[1]*a[0])

    return max_prod