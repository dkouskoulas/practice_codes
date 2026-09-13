
# time compelxity O(n log n)
# space complexity: O(1), O(n)

import heapq

def sheapsort(arr):

    heap = []

    for num in arr:
        heapq.heappush(heap, num)
    sorted_arr = [heapq.heappop(heap) for _ in range(len(arr))]

    return sorted_arr