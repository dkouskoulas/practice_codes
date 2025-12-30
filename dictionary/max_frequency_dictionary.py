

from collections import defaultdict

freq_dict= defaultdict(int)

nums = [ 1, 2, 3, 1, 1, 10,10,10,10,10,10,1012,13,3, 5, 6, 2, 3,10]
for num in nums:
    freq_dict[num] += 1

values = sorted(set(freq_dict.values()))

print(values[-3:])

