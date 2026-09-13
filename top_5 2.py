

def subarray_sum_equals(nums, k):
    if not nums:
        return None

    prefix_sum = 0
    count = 0
    pref_freq = {0:1}

    for num in nums:
        prefix_sum += num
        complement = prefix_sum - k
        count += pref_freq.get(complement,0)
        pref_freq[prefix_sum] = pref_freq.get(prefix_sum,0) + 1

    return count


def subarray_divisible_k(nums, k):
    if not nums:
        return None

    prefix_sum = 0
    count = 0 
    pref_freq = {0:1}

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum %k
        count += pref_freq.get(remainder,0)
        pref_freq[remainder] = pref_freq.get(remainder,0) + 1 
    
    return count


def count_paris(nums, k):
    if not nums:
        return None

    count = 0
    rem_freq = {0:1}

    for num in nums:
        rem = num % k

        complement = (k - rem) % k

        count += rem_freq.get(complement,0)
        rem_freq[rem] = rem_freq.get(rem,0) + 1

    return count

def longest_wo_repeating(nums):

    if not nums:
        raise ValueError('missing input')

    from collections import defaultdict

    seen = defaultdict(int)
    left = 0
    max_len = float('-inf')

    for right, char in enumerate(nums):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1 
        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len 


def peak_element(nums):
    if not nums:
        raise ValueError('missing input')

    left, right = 0, len(nums)-1

    while left < right:
        mid = (left + right)//2
        if nums[mid] < nums[mid+1]:
            left = mid + 1 
        else:
            right = mid

    return left



def meeting_rooms_ii(intervals):
    if not intervals:
        return 0

    starts = sorted([s for s, e in intervals])
    ends = sorted([e for s, e in intervals])

    s = 0
    e = 0 

    rooms = 0
    max_rooms = 0

    while s < len(intervals):
        if starts[s] < ends[e]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s+= 1
        else:
            rooms -= 1
            e += 1 

    return max_rooms



import heapq

def kth_largest(nums, k):
    if not nums or k<= 0 or k > len(nums):
        raise ValueError("invalid input")

    
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


def kth_smallest(nums, k):
    if not nums or k <= 0 or k > len(nums):
        raise ValueError('input issue')

    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return(-max_heap[0])