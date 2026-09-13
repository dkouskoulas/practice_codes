
import heapq 

def kth_extreme(arr, k, extrema = 'smallest'):

    assert arr, 'missing array'

    assert 1 <= k <= len(arr), 'length mismatch'
    assert extrema in ('smallest', 'largest'), 'INvalid input adjective'

    heap = []

    if extrema == 'smallest':

        for num in arr:
            heapq.heappush(heap, -num)
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return -heap[0]

    else:

        for num in arr:
            heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

        return heap[0]