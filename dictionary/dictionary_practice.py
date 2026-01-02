

nums = [1, 3, 3, 4, 2, 5, 5, 5, 8, 9, 10, 2, 2]

my_dict = {}

for num in nums:
    my_dict[num] = my_dict.get(num,0) + 1

print(my_dict) 
print(my_dict.values())
print(my_dict.keys())

nums = list(my_dict.values())
print(nums)
print(nums[3])

from collections import heapq

def kth_largest(nums,k):

    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)

    return min_heap

