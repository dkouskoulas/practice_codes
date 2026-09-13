
# code gives prefix values and hte final running_sum
def return_prefix(arr):

    prefix = []
    running_sum = 0 

    for num in arr:
        running_sum += num
        prefix.append(running_sum)

    return prefix, running_sum
