

from collections import defaultdict

my_dict = defaultdict()

array =[[1,2,5], [4, 3], [1,2, 5, 3], [1,2], [3]]

for x,y in enumerate(array):
        my_dict[x] = y

for key in my_dict:
    my_dict[key] = sum(my_dict[key])

print(my_dict)