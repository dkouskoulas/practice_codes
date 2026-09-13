

def find_missing_number(arr):
    if not arr:
        return None  # Return None for an empty array

    n = len(arr) + 1  # Total numbers including the missing one
    total_expect = n * (n + 1) // 2  # Sum of first n natural numbers
    total_seen = sum(arr)  # Sum of the given numbers

    return total_expect - total_seen  # The missing number
    
if __name__ == "__main__":

    test = [1, 2, 4]
    print(f'Test is {test}')
    print(f'The missing nubmer is {find_missing_number(test)}')