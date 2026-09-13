

def max_product(nums):

    max_prod = min_prod = result = nums[0] 

    for num in nums[1:]:
        candidates = (num, min_prod*num, max_prod*num)
        min_prod = min(candidates)
        max_prod = max(candidates)
        result = max(max_prod, result)


    return result