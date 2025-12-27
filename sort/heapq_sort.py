from heapq import heappush, heappop, heapify

def heapq_sort(nums):

    heap = []

    for num in nums:
        heappush(heap,num)


    return [heappop(heap) for _ in range(len(heap))]
