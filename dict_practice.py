
dict = {
'key1' : 4, 
'key2' : 3,
'key3' : 6,
'key4' : 5,
'key5' : 5,
'key6' : 1,
'key7' : 10, 
'key10': 13,
}


values = sorted(list(set(dict.values())))
print(values)


max_freqs = values[-3:]

print([key for key in dict.keys() if dict[key] in max_freqs])



