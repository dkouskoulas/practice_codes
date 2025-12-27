

def SMA(arr,k):
    n = len(arr)

    if n < k:
        raise ValueError('Length and window size mismatch')
    
    window_sum = sum(arr[:k])
    forecast = [window_sum//k]

    for i in range(k,n):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        forecast.append(window_sum//k)

    return forecast


def find_pivot(arr):

    n = len(arr)


    if arr[0] <= arr[n-1]:
        return -1

    left, right = 0, n - 1 

    while left < right:
        mid = (left + right)//2
        if arr[mid] > arr[right]:
            left = mid + 1 
        else:
            right = mid 
    return left

def max_subarray(nums):

    max_global = max_local = nums[0]

    for num in nums[1:]:
        max_local = max(num, max_local + num)
        max_global = max(max_global, max_local)

    return max_global

def min_subarray(nums):
    
    nums = [-x for x in nums]

    max_global = float('-inf')
    max_local = nums[0]

    for num in nums[1:]:
        max_local = max(num, max_local + num)
        max_global = max(max_global, max_local)

    return -max_global

def circular_var(nums):

    #calculate min and max from linear
    max_kadane = max_subarray(nums)
    if max_kadane < 0:
        return max_kadane
    min_kad = min_subarray(nums)
    
    total_sum = sum(nums)
    max_circular = total_sum - min_kad

    return max(max_kadane, max_circular)