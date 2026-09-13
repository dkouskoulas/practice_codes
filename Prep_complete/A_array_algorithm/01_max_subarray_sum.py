

def max_subarray_sum(arr):
    if not arr:
        return None

    cur_max = global_max = arr[0]

    for num in arr[1:]:
        cur_max = max(num, cur_max + num)
        global_max = max(cur_max, global_max)

    return global_max 


if __name__ == "__main__":

    test = [2, 1, -3, 5, 2, 3]
    print(f'Testing on {test}')
    print(f'The max subarray sum is {max_subarray_sum(test)}')