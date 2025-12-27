

def permutations(arr):

    if len(arr) <= 1:
        return [arr]
    
    result = []

    for i in range(len(arr)):

        rest = arr[:i] + arr[i+1:]
        for perm in permutations(rest):
            result.append([arr[i]]+perm)

    return result