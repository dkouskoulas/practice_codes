# O (logn)
# sapce compelx O(1)

def binary_search(nums, k):

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right)//2
        if nums[mid] == k:
            return mid
        elif nums[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1
