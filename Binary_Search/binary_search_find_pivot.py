
def find_pivot(arr):
    n = len(arr)

    #define left and right pointers

    left, right = 0, n - 1

    # if this condition is satisfied the array is not rotated and there is no pivot
    if arr[left] < arr[right]:
        return 0 

    # if array is rotated, find the pivot using binary search
    while left < right:
        #define a mid point for the binary search approach
        mid = (left + right)//2
        
        #if the array at the mid point is greater than the rightmost entry (as defined), the pivot is to the right
        if arr[mid] > arr[right]:
            left = mid + 1
        #the right half is sorted, so pivot must be in left half (or at mid)
        else:
            right = mid 
    #left and right converge to the pivot index
    return left 