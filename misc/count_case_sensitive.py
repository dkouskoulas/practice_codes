
def count_cases(input_string):

    count_lower_case = 0
    count_upper_case = 0

    for s in input_string:
        if s.islower():
            count_lower_case += 1
        elif s.isupper():
            count_upper_case += 1
        else:
            pass

    return count_upper_case - count_lower_case
