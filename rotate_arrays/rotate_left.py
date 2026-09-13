
def rotate_left_slice(arr, k):
    n = len(arr)
    k = k % n

    return arr[k:] + arr[:k]
