from collections import defaultdict, Counter

# Sample dictionary
my_dict = {1: 10, 2: 20, 3: 30, 4: 40}

# 1. Check if key exists
if 1 in my_dict:
    print("Key 1 exists")

# 2. Get with default (avoid KeyError)
value = my_dict.get(5, 0)  # Returns 0 if key 5 doesn't exist
print(f"Value for key 5: {value}")

# 3. Delete key
del my_dict[4]
# Or: my_dict.pop(4)  # Returns value while deleting
# Or: my_dict.pop(4, None)  # Returns None if key doesn't exist

# 4. Update/merge dictionaries
other_dict = {5: 50, 6: 60}
my_dict.update(other_dict)
# Or in Python 3.9+: my_dict |= other_dict

# 5. Dictionary comprehension
squared = {k: v**2 for k, v in my_dict.items()}
filtered = {k: v for k, v in my_dict.items() if v > 20}

# 6. Sort dictionary by key or value
sorted_by_key = dict(sorted(my_dict.items()))
sorted_by_value = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# 7. Reverse key-value pairs (if values are unique)
reversed_dict = {v: k for k, v in my_dict.items()}

# 8. Count frequency using Counter
array = [1, 2, 3, 4, 4, 4, 5, 1, 2]
freq = Counter(array)
print(f"Most common: {freq.most_common(2)}")  # [(4, 3), (1, 2)]

# 9. Default dict with list (grouping)
grouped = defaultdict(list)
for num in [1, 2, 3, 4, 5, 6]:
    grouped[num % 2].append(num)  # Group by even/odd
print(f"Grouped: {dict(grouped)}")  # {1: [1, 3, 5], 0: [2, 4, 6]}

# 10. setdefault (get or set default)
my_dict.setdefault(10, 100)  # Sets key 10 to 100 if not exists

# 11. Clear all items
# my_dict.clear()

# 12. Copy dictionary
shallow_copy = my_dict.copy()
import copy
deep_copy = copy.deepcopy(my_dict)

print(my_dict)