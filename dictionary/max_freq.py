# Hash Map - Find Element with Maximum Frequency
# Time Complexity: O(n) - single pass to count + O(n) to find max
# Space Complexity: O(n) - hash map stores unique elements


array =[1,2,5,4, 3]

freq_dict = {}

for num in array:
    freq_dict[num] = freq_dict.get(num,0)+1

print('dict is:',freq_dict)