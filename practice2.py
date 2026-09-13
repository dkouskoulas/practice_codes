
def pair_sum_divisible(nums, k):

    seen = set()

    for num in nums:

        remainder = num % k 
        needed = (k - remainder) % k 

        if needed in seen:
            return True

        seen.add(remainder)

    return False 

def pair_wise_sum_Divisible(nums, k):

    seen = {}

    for idx, num in enumerate(nums):
        remainder = nums % k 
        needed = (k - remainder) % k 
        if needed in seen:
            return seen[needed], idx

        seen[remainder] = idx


def top_k_freq(words, k):

    if not words:
        return -1

    from collections import defaultdict

    freq_dict = defaultdict(int)

    for word in words:
        freq_dict[word] += 1 
    
    word_list = [[key,val] for key, val in freq_dict.items()]

    word_list.sort(key = lambda x: (-x[1],x[0]))

    return [x[0] for x in word_list[:k]]

def prod_array_except_self(nums):

    n = len(nums)

    result = [1] * len(nums)

    prefix = 1 
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]


    suffix = 1 
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


def max_subarray(nums):

    cur_max = global_max = nums[0] 

    for num in nums:
        cur_max = max(num, cur_max + num)
        global_max = max(cur_max, global_max)


    return global_max 


def buy_sell_stock(prices):

    min_price = float('inf')
    max_profit = float('-inf')

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max_profit(max_profit, price - min_price)

    return max_profit


def max_avg_subarray(nums, k):

    window = sum(nums[:k])
    window_avg = window/k
    max_avg = window_avg 

    for i in range(k,len(nums)):
        window += nums[i] - nums[i-k]
        window_avg = window/k 
        max_avg = max(max_avg, window_avg)

    return max_avg


def longest_wo_repeating(nums):

    from collections import defaultdict 

    max_len = 0
    seen = defaultdict(int)
    left = 0 

    for right, char in enumerate(nums):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1 

        seen[char] = right
        max_len = max(max_len, right - left + 1 )

    return max_len



    def min_size_subarray_sum(nums, target):

        left = 0 
        window_sum = 0
        min_size = float('inf')

        for right in range(nums):

            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)

                window_sum -= nums[left]
                left+= 1 

        return 0 if min_len == float('inf') else min_len


    def sliding_window_max(nums,k):

        from collections import deque
        
        max_vals = [] 
        window = deque(nums[:k])
        max_vals.append(max(window))

        for i in range(k,len(nums)):
            window.popleft()
            window.append(nums[i])
            max_vals.append(max(window))

        return max_vals


    def merge_intervals(intervals):

        intervals.sort(key = lambda x: x[0])

        merged_intervals = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged_intervals[-1][1]
            if start <= last_end:
                merged_intervals[-1][1] = max(last_end, end)
            else:
                merged_intervals.append([start,end])

        return merged_intervals 

    
    def meeting_rooms(intervals):

        intervals.sort(key = lambda x: x[0])
        meetings_passed = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = meetings_passed[-1][1]
            if last_end > start:
                return False
            meetings_passed.append([start,end])
    
        return True
            

    def closest_to_origin(coords, k):

        from collections import defaultdict

        distances_dict = defaultdict(int)

        for x,y in coords:
            distance = x**2 + y**2 
            distances_dict[(x,y)] = distance

        pairs_list = [[x,y] for x, y in distances_dict.items()]
        pairs_list.sort(key = lambda x: (x[1], x[0]))

        final_list = pairs_list[:k]

        return [x[0] for x in final_list]

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

    def find_peak(nums):

        left, right = 0, len(nums) - 1 

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1 
            else: 
                right = mid
        return left
    

    def k_closest_points(coords):

        coords_list = []

        for x,y in coords:
            distance = x**2 + y**2 
            coords_list.append([[x,y],distance])

        coords_list.sort(key = lambda x: x[1])

        return [x[0] for x in coords_list[:k]]




    def max_depth(root):

        if not root:
            return None

        left = max_depth(root.left)
        right = max_depth(root.right)


        return 1 + max(left,right)


    def is_valid_bst(root):

        def dfs(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return (dfs(node.left, low, node.val) 
                    and dfs(node.right, node.val, high)
                        )
        return dfs(root, float('-inf'), float('inf'))


    def min_meeting_rooms(intervals): 
        if not intervals:
            return 0

        starts = sorted([s for s,e in intervals])
        ends = sorted([e for s, e in intervals])

        rooms = 0
        end_ptr = 0

        for start in starts:
            if start < ends[end_ptr]:
                rooms += 1 
            else:
                end_ptr -= 1 

        return rooms



    def longest_wo_repeating(nums):

        from collections import defaultdict

        seen = defaultdict(int)
        left = 0
        max_len = 0

        for right, char in enumerate(nums):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1 
            seen[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len


    def longest_sequence(s):

        count = 1
        max_count = 1

        for i in range(1, len(s)):

            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1

            max_count = max(max_count, count)

        return max_count


    def RLE(s):

        result = []
        count = 1

        for i in range(1, len(s)):

            if s[i] == s[i-1]:
                count += 1 

            else:
                result.append(str(count) + s[i-1])
                count = 1 

        result.append(str(count) + s[i-1])

        return ''.join(result)
