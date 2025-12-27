# Heap Sort using heapq
# Time Complexity: O(n log n) - n insertions/deletions in heap
# Space Complexity: O(n) - heap stores all elements

from heapq import heappush, heappop, heapify

def heapq_sort(nums):

    heap = []

    for num in nums:
        heappush(heap, num)

    return [heappop(heap) for _ in range(len(heap))]
