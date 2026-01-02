

def kadane_min(nums):
    
    inv = [-x for x in nums]

    max_local = max_global = float('-inf')

    for num in inv:
        max_local = max(num, max_local + num)
        max_global = max(max_local, max_global)


    return -max_global