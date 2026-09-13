

def max_product_subarray(arr):

    if not arr:
        return 0

    max_product = min_product = result = arr[0]

    for num in arr[1:]:
        candidates = (num, min_product * num , max_product * num)
        min_product = min(candidates)
        max_product = max(candidates)
        result = max(max_product, result)
    return result


if __name__ == "__main__":
    
    arr = [1, 3, 6, -2, 3, 9]

    print(f'max product of array: {max_product_subarray(arr)}')
