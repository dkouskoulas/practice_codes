

nums = [1, 3, 4, 5, 5, 3, 2, 1, 2, 3]


from collections import defaultdict

freq_dict = defaultdict(int)

for idx,num in enumerate(nums):
    freq_dict[num] += 1 

print(freq_dict)
