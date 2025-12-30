
# arr.sort()

# Quicksort Algorithm
# Time Complexity: 
#   - Best/Average: O(n log n)
#   - Worst: O(n²) when pivot is always smallest/largest (unbalanced partitions)
# Space Complexity: O(n) due to list comprehensions (not in-place)
# Note: This implementation uses extra space for clarity; in-place quicksort is O(log n) space

def quicksort(arr):

    if len(arr) < 2:
        return arr
    
    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)
