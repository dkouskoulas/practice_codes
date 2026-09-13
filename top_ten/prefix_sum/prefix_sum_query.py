

def prefix_sum_query(arr, queries):

    #calculate the prefix sums 
    prefix = []
    running_sum = 0 

    for num in arr:
        running_sum += num
        prefix.append(running_sum)

    list_of_sums = []

    #for i in range(len(queries)):
    #    l, r = queries[i][0], queries[i][1]
    #    if l == 0:
    #        list_of_sums.append(prefix[r])
    #    else: 
    #        list_of_sums.append(prefix[r]-prefix[l-1])

    for l, r in queries:
        if l == 0:
            list_of_sums.append(prefix[r])
        else:
            list_of_sums.append(prefix[r]-prefix[l-1])

    return list_of_sums