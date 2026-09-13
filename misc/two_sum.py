

def two_sum(arr, k):


    seen = {}

    for i, num in enumerate(arr):

        complement = k - num 

        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return False