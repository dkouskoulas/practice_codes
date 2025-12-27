
import heapq 

def max_triple_prod(arr):

    a = heapq.nlargest(3, arr)
    b = heapq.nsmallest(2, arr)

    max_prod = max(a[0]*a[1]*a[2],b[0]*b[1]*a[0])

    return max_prod