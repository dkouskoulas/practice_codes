def find_pivot(nums):

    left, right = 0, len(nums) - 1

    if nums[left] <= nums[right]:
        return 0 
    
    while left < right:

        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1 

        else:
            right = mid 

    return left 


def search_rotated(nums, target):

    if not nums:
        return ValueError('No nums array')
    
    n = len(nums)

    pivot = find_pivot(nums)

    if nums[pivot] <= target <= nums[n-1]:
        left, right = pivot, n - 1

    else:
        left, right = 0, pivot - 1

    while left <= right:
        mid = (left + right)//2

        if nums[mid] == target:
            return mid 
        
        if nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1 

    return - 1 

if __name__ == "__main__":

    arr = [2, 3, 4 , 5, 0, 1]

    result_1 = find_pivot(arr)
    result_2 = search_rotated(arr, 1)

    print(result_1, result_2)