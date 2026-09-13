from collections import defaultdict 

def two_sum(nums, target):

    if not nums:
        return 0 

    seen = defaultdict(int)

    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx

    return -1
    

def pair_wise_divisible(nums, k):

    if not nums: 
        return 0 

    prefix_sum  = 0
    count = 0
    pref_freq = {0:1}

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k
        count += pref_freq.get(remainder,0)
        pref_freq[remainder] = pref_freq.get(remainder,0) + 1 # HAD ERROR

    return count


def count_arrays_sum_k(nums, k):
    if not nums:
        return -1 

    prefix_sum= 0
    count = 0 
    pref_freq = {0:1}

    for num in nums:
        prefix_sum += num
        complement = prefix_sum - k
        count += pref_freq.get(complement, 0)
        pref_freq[prefix_sum] = pref_freq.get(prefix_sum,0) + 1 # HAD ERROR
    return count 


def top_k_freq(nums, k):

    if not nums:
        return 0

    frequency_dictionary = defaultdict(int)

    for num in nums:
        frequency_dictionary[num] += 1 

    num_frequency_pairs = [[key, val] for key, val in frequency_dictionary.items()]

    num_frequency_pairs.sort(key = lambda x: (-x[1], x[0]))

    top_k_numbers = [x[0] for x in num_frequency_pairs[:k]]

    return top_k_numbers

def product_array_self(nums):

    #validate inputs
    if not nums:
        return 0

    result = [1]*len(nums)

    prefix = 1 
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]

    suffix = 1 
    for i in range(len(nums)-1,-1,-1):# HAD ERROR
        result[i] *= suffix
        suffix *= nums[i]

    return result

def max_subarray(nums):

    if not nums:
        raise ValueError('missing or empty input')

    cur_max = global_max = nums[0] 

    for num in nums[1:]:# HAD ERROR
        cur_max = max(num, cur_max + num)
        global_max = max(global_max, cur_max)

    return global_max


def best_time_buysell(prices):

    if not prices:
        raise ValueError('empty or missing input')

    min_price = float('inf')
    max_profit = float('-inf')

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

def max_avg_subarray(nums,k):
    if not nums:
        raise ValueError('missing nums')

    window = sum(nums[:k]) # HAD ERROR
    cur_avg = window/k
    max_avg = cur_avg

    for i in range(k, len(nums)):
        window += nums[i] - nums[i-k]
        cur_avg = window/k
        max_avg = max(cur_avg, max_avg)

    return max_avg


def longest_wo_repeat(nums):

    if not nums:
        raise ValueError('missing or empty input')

    from collections import defaultdict

    seen = defaultdict(int)
    left = 0
    max_len = float('-inf')

    for right, char in enumerate(nums): #HAD ERROR
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = idx
        max_len = max(max_len, right - left + 1)

    return max_len if max_len != float('-inf') else max_len #HAD ERROR

##### STRUGGLE WITH THIS##################
def minimize_size_subarray_sum(nums, k):

    if not nums:
        raise ValueError('missing or empty input')

    min_len = float('inf')

    window_sum = 0
    left = 0

    for right in range(len(num)):

        window_sum += nums[right]

        while window_sum >= k:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]

            left += 1

    return min_len if min_len != float('inf') else 0


def sliding_window_max_collect(nums, k):

    if not nums:
        raise ValueError('missing input or empty')

    from collections import deque

    max_values = [] # HAD ERROR
    window= deque(nums[:k]) # HAD ERROR
    max_values.append(max(window))

    for i in range(k,len(nums)):
        window.popleft()
        window.append(nums[i])
        max_values.append(max(window))

    return max_values


def merge_intervals(intervals):

    intervals.sort(key = lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]: #HAD ERRPR
        last_end = merged[-1][1]
        if start <= last_end: #HAD ERRPR
            merged[-1][1] = max(last_end, end) #HAD ERRPR
        else:
            merged.append([start,end])

    return merged


def meeting_rooms_I(intervals):

    if not intervals:
        raise ValueError("missing or empty data")

    intervals.sort(key = lambda x: x[0])
    passed = [intervals[0]]

    for start, end in intervals[1:]: #HAD BUG
        last_end = passed[-1][1]
        if start < last_end:
            return False
        passed.append([start,end])

    return True

def k_closest_to_origin(coords, k):
    if not coords:
        raise ValueError('missing or empty input')

    coord_distance_pairs = [[x, x[0]**2 + x[1]**2] for x in coords]

    coord_distance_pairs.sort(key = lambda x: (x[1], x[0]))

    k_closest_coords = [x[0] for x in coord_distance_pairs[:k]]

    return k_closest_coords

def binary_search(nums, target):

    left, right = 0, len(nums) - 1 

    while left <= right: 
        mid = (left + right)//2 
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
    return -1 


#MUST LEANR 

def find_peak(nums):

    left, right = 0, len(nums) - 1 

    while left < right:
        mid = (left + right)//2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1 
        else:
            right = mid

    return left

