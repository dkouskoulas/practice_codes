

def rotate_array(arr, k, direction = 'left'):

    if not arr: 
        raise ValueError('Missing array!')
    
    n = len(arr)
    k = k % n
    
    if direction == 'left':
        return arr[k:] + arr[:k]
    elif direction == 'right':
        return arr[-k:] + arr[:-k]
    
    raise ValueError('Invalid direction!')

