


def product_expcept_k(arr, k):

    left_prod = 1
    for num in arr[:k]:
        left_prod = left_prod*num

    right_prod = 1
    for num in arr[k+1:]:
        right_prod = right_prod*num

    return left_prod*right_prod