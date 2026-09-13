

def count_sum_k(nums, k):
    if not nums:
        return None

    prefix_sum = 0
    count = 0
    pref_freq = {0:1}

    for num in nums:
        prefix_sum += num
        complement = prefix_sum - target
        count += pref_freq.get(complement,0)
        pref_freq[prefix_sum] = pref_freq.get(prefix_sum,0) + 1 

    return count


def longest_connsecutive_sequence(nums):
    if not nums:
        return 0 

    num_set = set(nums)
    max_len = 0 

    for num in num_set:
        if num - 1 in set:
            current = num
            length = 1 
            if num + 1 in set:
                current += 1
                length += 1 

    max_len = max(max_len, length)

    return max_len


    def prod_except_self(nums):
        if not nums:
            raise ValueError("missing input")

        result = [1]*len(nums)

        prefix = 1 
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]

    
        return result

    def search_rotated(nums, target):
        if not nums:
            return None 

        left, right = 0, len(nums) - 1 

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return target

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 
                else:
                    left = mid + 1 
            else:
                if nums[mid] < target <= nums[right]:
                    right = mid + 1 
                else:
                    left = mid -1

    from collections import defaultdict

    def top_K_frequent_elements(nums, k):
        if not nums:
            raise ValueError("missing input array")

        frequency_dictionary = defaultdict(int)

        for num in nums:
            frequency_dictionary[num] += 1 
    
        pair_list = [[key, val] for key, val in frequency_dictionary.items()]
        pair_list.sort(key = lambda x: (-x[1], x[0]))

        return [x[0] for x in pair_list[:k]]