def get_intersection(a, b):
 
    set_a = set(a)
    set_b = set(b)

    if len(set_a) < len(set_b):
        return [x for x in set_a if x in set_b]
    else:
        return [x for x in set_b if x in set_a]
