"""
Maximum Length Bitonic Subarray

Given an array of integers, find the length of the longest contiguous subarray
that first monotonically increases and then monotonically decreases.

A bitonic subarray may be:
- strictly increasing only, or
- strictly decreasing only, or
- increasing followed by decreasing.

Return the maximum length of such a subarray.

Notes:
- The subarray must be contiguous.
- The peak element (where increasing changes to decreasing) is counted once.
- If the array is empty, return 0.

Example:
Input:  [12, 4, 78, 90, 45, 23]
Output: 5
Explanation: The longest bitonic subarray is [4, 78, 90, 45, 23]
"""



def max_len_bitonic_subarray(arr):

    if not arr:
        return 0 
    
    n = len(arr)
    max_len = 1 
    i = 0 

   
    while i < n - 1:

        inc_len = 1
        while i < n - 1 and arr[i] < arr[i+1]:
            inc_len += 1 
            i += 1 
        
        dec_len = 0 
        while i < n - 1 and arr[i] > arr[i+1]:
            dec_len += 1 
            i += 1


        # if boht sides msut be present 
        if inc_len > 1 and dec_len > 0: 
            max_len = max(max_len, inc_len + dec_len)

        while i < n - 1 and arr[i] == arr[i + 1]:
            i += 1 
    return max_len