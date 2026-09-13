def count_sum_K(nums,k):
    if not nums:
        raise ValueError("missing input array")

    prefix_sum = 0
    pref_freq = {0:1}
    count = 0

    for num in nums:
        prefix_sum += num
        complement = prefix_sum - k
        count += pref_freq.get(complement,0)
        pref_freq[prefix_sum] = pref_freq.get(prefix_sum,0) + 1

    return count


def consec_seguence(nums):
    if not nums:
        return 0 

    num_set = set(nums)
    max_len = 0

    for num in num_set:
        if num -1 in num_set:
            current = num
            length = 1 
            if num + 1 in num_set:
                current += 1 
                length += 1 
    max_len = max(length, max_len)


    return max_len


def prod_except_self(nums):

    if not nums:
        raise ValueError('missing nums array')

    result = [1]*len(nums)

    prefix = 1 
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]

    suffix = 1 
    for i in range(len(nums) - 1, -1 ,-1);
        result[i] *= suffix 
        suffix *= nums[i]

    return result


def search_rotated_array(nums, target):
    if not nums:
        raise ValueError('missing input array')

    left, right = 0, len(nums) - 1 

    while left <= right:
        mid = (left + right) // 2 

        if nums[mid] == target:
            return mid 

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1 
            else:
                left = mid + 1 
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1 
    return -1


def binary_search(nums):
    if not nums:
        raise ValueError('missing input array')

    left, right = 0, len(nums) - 1 

    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return True 
        if nums[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
    return False

def kth_smallest(nums,k):
    if not nums:
        raise ValueError("missing input array")

    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return -max_heap[0]

def kth_largest(nums, k):
    if not nums:
        raise ValueError('missing input')

    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


def meeting_rooms_II(intervals):
    if not intervals:
        return 0 

    starts = sorted([s for s,e in intervals])
    ends = sorted([e for s,e in intervals])

    s = 0
    e = 0 
    max_rooms = 0

    while s < len(intervals)
        if starts[s] < ends[e]:
            rooms += 1 
            max_rooms = max(max_room, rooms)
        else:
            rooms -= 1 
            e += 1 

    return max_rooms


def min_Subarray_len(nums, k):
    left = 0
    cur_sum = 0
    best = float('inf')

    for right in range(len(nums)):
        cur_sum += nums[right]

        while cur_sum >= k:
            best = min(best, right - left + 1)
            cur_sum -= nums[left]
            left += 1
    
    return best if best != float('inf') else 0


def valid_parentheses(s):
    stack = [] 

    pairs = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for char in s:

        if char in '([{':
            stack.append(char)

        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0