
from heapq import heapify 


def heapq_sort(nums):
    heap = nums.copy()
    heapify(heap)

    return [heappop(heap) for _ in range(len(heap))]