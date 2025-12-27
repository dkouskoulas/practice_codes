# Recursion - Generate All Permutations
# Time Complexity: O(n! * n) - n! permutations, each takes O(n) to build
# Space Complexity: O(n! * n) - stores all permutations


def permutations(arr):

    if len(arr) <= 1:
        return [arr]
    
    result = []

    for i in range(len(arr)):

        rest = arr[:i] + arr[i+1:]
        for perm in permutations(rest):
            result.append([arr[i]]+perm)

    return result