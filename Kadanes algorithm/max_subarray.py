


def max_subarray_sum(nums):

    max_global = max_local = float('-inf')

    for num in nums:
        max_local = max(num, max_local + num)
        max_global = max(max_global, max_local)

    return max_global


if __name__ == "__main__":
    arr = [1, 3, 5, -1, 8, 10, 12]

    result = max_subarray_sum(arr)
    print(result)

