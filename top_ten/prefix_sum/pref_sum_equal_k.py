
def sum_equal_k(arr, k):

    prefix_sum = 0
    pref_freq = {0:1}
    count = 0

    for num in arr:
        prefix_sum += num
        complement = prefix_sum - k
        count += pref_freq.get(complement,0) 
        pref_freq[prefix_sum] = pref_freq.get(prefix_sum,0) + 1


    return count 