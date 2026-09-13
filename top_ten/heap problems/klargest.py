
import heapq


def k_largest(nums, k):

    heap = []

    for num in nums:
        heapq.heappush(heap,num)

        if len(heap) > k:
            heapq.heappop(heap)


    return heap


if __name__ == "__main__":

    nums = [3, 1, 5, 12, 2, 11, 4]

    k = 3 

    top_k = k_largest(nums, k)

    print(k_largest(nums, k))
    print (top_k[0])

