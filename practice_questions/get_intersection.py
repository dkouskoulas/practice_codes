# Set Intersection - Find Common Elements
# Time Complexity: O(min(m, n)) where m, n are lengths of arrays
# Space Complexity: O(m + n) - two sets created

def get_intersection(a, b):
 
    set_a = set(a)
    set_b = set(b)

    if len(a) < len(b):
        return [x for x in set_a if x in set_b]
    else:
        return [x for x in set_b if x in set_a]
