

def find_leader(arr):
    if not arr:
        raise ValueError('Missing array!')
    
    leaders = []
    cur_max = float('-inf')

    for num in reversed(arr):
        if num >= cur_max:
            leaders.append(num)
            cur_max = num
    return leaders[::-1]
