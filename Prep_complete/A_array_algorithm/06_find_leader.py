

def find_leader(arr):

    if not arr:
        raise ValueError('Missing array!')
    
    arr_reverse = arr[::-1]

    leaders = [arr_reverse[0]]
    cur_max = arr_reverse[0]

    for num in arr_reverse[1:]:
        if num >= cur_max:
            leaders.append(num)
        cur_max = max(cur_max, num)

    return leaders[::-1]


if __name__ == "__main__":
    arr = [26, 7, 3, 8, 24, 2, 2, 1, 20]

    print(find_leader(arr))


    