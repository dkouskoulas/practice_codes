""""

Time O(n * log(n)), worst n**2


"""

import random 


def quicksort(arr):

    if not arr:
        raise ValueError('missing array!')

    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x== pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)
    