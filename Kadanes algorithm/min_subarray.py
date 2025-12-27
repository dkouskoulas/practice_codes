# Kadane's Algorithm Variant - Minimum Subarray Sum
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(n) - creates inverted array

def min_subarray(arr):

    inv = [-x for x in arr]

    max_global = max_local = inv[0]

    for num in inv:
        max_local = max(num, max_local + num)
        max_global = max(max_global, max_local)

    return -max_global


if __name__ == "__main__":
    arr = [1, 2, 3, -5, -4, 3, 2, 1, 2, 10, 12, -20, 4, 3]
    result = min_subarray(arr)
    print(result)

