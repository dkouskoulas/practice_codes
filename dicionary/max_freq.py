

array =[1,2,5,4, 3]

freq_dict = {}

for num in array:
    freq_dict[num] = freq_dict.get(num,0) + 1

print(freq_dict)

keys = freq_dict.keys()
values = freq_dict.values()

print([key for key, val in freq_dict.items() if val == max(values)])