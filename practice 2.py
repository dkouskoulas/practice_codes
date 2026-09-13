s = "abcabcbb"


def longest_wo_repeating(s):
    if not s: 
        return 0 

    seen = {}
    max_len = 0
    left = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1 
        seen[char] = right
        max_len = max(max_len, right - left + 1 )

    return max_len



words = ["eat","tea","tan","ate","nat","bat"]

from collections import Counter
from collections import defaultdict

def group_anagrams(words):
    if not words:
        return 0 

    grouped = defaultdict(list)
    
    for word in words:
        key = tuple(sorted(word))
        grouped[key].append(word)

    result = [val for key, val in grouped.items()]

    return result

def prod_except_self(nums,i):
    if not nums:
        return 0 
    
    left_branch = nums[:i]
    right_branch = nums[i+1:]

    left_prod = 1
    for num in left_branch:
        left_prod *= num

    right_prod = 1 
    for num in right_branch:
        right_prod *= num

    return left_prod*right_prod



def prod_except_self(nums):

    n = len(nums)

    result = [1] * n 

    prefix = 1 

    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1 

    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


def prefix_sum(nums):

    result = []
    running_sum = 0

    for num in nums:
        running_sum += num
        result.append(running_sum)
        
    return result
    

def prefix_sum(nums,k):

    prods = []
    running_prod = 1 

    for num in nums[:k]:
        running_prod *= num
        prods.append(running_prod)

    return prods



def prod_except_self(nums):

    n = len(nums)

    result = [1]*n

    prefix = 1 

    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1 

    for i in range(n-1,-1,-1):
        result[i]*= suffix
        suffix *= nums[i]

    return result


def is_valid_parentheses(s):

    stack = []

    mapping = {

        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for char in s:

        if char in "([{":
            stack.append(char)

        else:
            if not stack:
                return False

            top = stack.pop()

            if top != mapping[char]:
                return False

    return len(stack) == 0


def two_sum(nums, target):
    if not nums:
        return 0 

    seen = {}

    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [idx, seen[complement]]
        seen[complement] = idx
    return -1
    

intervals = [[1,3],[2,6],[8,10],[15,18]]


def merge_intervals(intervals):

    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:

        last_end = merged[-1][1]

        if start_end <= last_end:
            merged[-1][1] = max(last_end, end)

        else:
            merged.append([start,end])

    return merged


def binary_search(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid - 1 
        else:
            right = mid + 1

    return - 1 



def best_time_buy(prices):

    min_price = float('inf')
    max_proft = float('-inf')

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit if max_profit != float('-inf') else 0



def max_subarry(nums):
    if not nums:
        return 0 

    cur_max = global_max = nums[0]

    for num in nums[1:]:
        cur_max = max(num, cur_max + num)
        global_max = max(global_max, cur_max)

    return global_max





from collections import defaultdict

def find_duplicate(nums):

    if not nums:
        return 0

    seen = defaultdict(int)

    for num in nums:
        if num in seen:
            return num
        seen[num] += 1 

    return -1

def floyds_cycle(node):

    slow = false = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

from collections import defaultdict

def top_k_freq(words,k):
    
    if not words:
        return 0

    freq_dict = defaultdict(int)

    for word in words:
        freq_dict[word] += 1 

    word_pairs = [[word, freq] for word, freq in freq_dict.items()]

    word_pairs_sorted = sorted(word_pairs, key = lambda x: (-x[1],x[0]))

    return [word for word in word_pairs_sorted[:k]]


def k_closest_points(coords,k):

    if not coords:
        return 0

    coord_tuples = [tuple(coord) for coord in coords]

    distance_dict = defaultdict(tuple)

    for idx, coord in enumerate(coord_tuples):
        distance = sqrt(coord[0]**2 + coord[1]**2)
        distance_dict[coord] = distance

    distances_list = [[key, val] for key, val in distance_dict.items()]

    distances_sorted = sorted(distances_list, key = lambda x: (x[1], x[0]))

    distances_smallest = distances_sorted[:k]

    return [distance[0] for distance in distances_smallest]


def k_closest_points(points, k):

    points_sorted = sorted(points, key = lambda x: p[0]**2 + p[1]**2)

    return points_sorted[:k]

    
def max_avg_contig(nums,k):
    if not nums:
        return 0 

    cur_avg = float('-inf')

    for i in range(len(nums)-k+1):
        window = nums[i:i+k]
        cur_avg = sum(window)/k
        max_avg = max(cur_avg, max_avg)

    return max_avg


def max_avg_contig(nums, k):

    window_sum = sum(nums[:k])

    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)


    return max_sum / k




def max_sum(nums, k):

    if not nums:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum