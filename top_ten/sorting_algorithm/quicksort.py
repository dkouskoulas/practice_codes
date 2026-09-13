#time compleity: O(n log n)
#space (log n)
import random 

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr)

    pivot = random.choice(arr)
   
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
