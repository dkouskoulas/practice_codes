# Heap Sort using heapq (Alternative)
# Time Complexity: O(n log n) - heapify O(n) + n deletions O(log n) each
# Space Complexity: O(n) - creates copy of array

from heapq import heapify, heappop


def heapq_sort(nums):
    heap = nums.copy()
    heapify(heap)

    return [heappop(heap) for _ in range(len(heap))]