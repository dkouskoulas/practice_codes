
import heapq

def kth_smallest(nums, k):
    max_heap = [-x for x in nums[:k]]

    heapq.heapify(max_heap)
    for num in nums[k:]:
        if num < -max_heap[0]:
            heapq.heappushpop(max_heap, -num)
            
    return -max_heap[0]