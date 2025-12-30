from collections import Counter

arr = [1, 2, 5, 2, 2, 2, 3, 10, 12, 12, 12, 12, 10, 8, 8, 8, 13]

counter = Counter(arr)
print(counter)

keys = counter.keys()
print(keys)

values = list(counter.values())
print('answer one:',sorted(set(values))[-3:])

print('test ',set(values))

def quick_sort(arr):

    if len(arr) < 2:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

test_b = sorted(set(values))
sorted_vals = quick_sort(test_b)
print(sorted_vals[::-1][:3])