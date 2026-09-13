

def rotate_right(arr, k):
    n = len(arr)
    k = k%n
    return arr[-k:] + arr[:-k]
