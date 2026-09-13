
import heapq 

def kth_smallest(nums,k):

    heap = []

    for num in nums:
        heapq.heappush(heap, -num)

        if len(heap) > k:
            heapq.heappop(heap)

    return [-x for x in heap], -heap[0]