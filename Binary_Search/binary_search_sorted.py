import numpy as np


def binary_search(arr, target):

    left, right = 0, len(arr) - 1 

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = np.random.randint(0, 100, size = 20)
    arr.sort()
    target = np.random.randint(0, 100)
    result = binary_search(arr, target)
    print(arr)

    if result == -1:
        print('The target number is not in the array.')
    else:
        print('The target number', target, 'is at index:', result)
