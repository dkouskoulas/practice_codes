
from collections import defaultdict

array =[[1,2,5], [4, 3], [1,2, 5, 3], [1,2], [3]]

my_dict = defaultdict(int)

for idx, val in enumerate(array):
    my_dict[idx] = val

for val in my_dict:
    my_dict[val] = sum(my_dict[val])

print(my_dict)

