
def divisible_k(arr, k):

    prefix_sum = 0 
    count = 0
    pref_freq = {0:1}

    for num in arr:
        prefix_sum += num 
        remainder = prefix_sum % k
        count += pref_freq.get(remainder,0)
        pref_freq[remainder] = pref_freq.get(remainder,0) + 1
        
    return count



def divisible_k(arr, k):
    
    prefix_sum = 0
    count = 0
    pref_freq = {0:1}

    for num in arr:
        prefix_sum += num
        remainder = prefix_sum % k
        count += pref_freq.get(remainder,0)
        pref_freq[remainder] = pref_freq.get(remainder,0) + 1 

    return count


def divisible_k(nums,k):

    prefix_sum = 0
    count = 0
    pref_freq = {0:1}

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum %k 
        count += pref_freq.get(remainder,0)
        pref_freq[remainder] = pref_freq.get(remainder,0) + 1

    return count


def sum_K(nums, k):
    prefix_sum = 0
    count = 0
    pref_freq = {0:1}

    for num in nums:
        prefix_sum += num
        complement = prefix_sum - k
        count += pref_freq.get(complement,0)
        pref_freq[prefix_sum] = pref_freq.get(prefix_sum,0) + 1

    return count


def find_subarray_sum_k(nums, k):

    prefix_sum = 0
    seen = {0: -1}

    for i, num in enumerate(nums):

        prefix_sum += num

        complement = prefix_sum - k

        if complement in seen:
            start = seen[complement] + 1
            end = i + 1
            return nums[start:end]

        seen[prefix_sum] = i

    return []


def find_subarray_indices(nums, k):

    prefix_sum = 0
    seen = {0: -1}

    for i, num in enumerate(nums):

        prefix_sum += num

        complement = prefix_sum - k

        if complement in seen:
            return [seen[complement] + 1, i]

        seen[prefix_sum] = i

    return [-1, -1]