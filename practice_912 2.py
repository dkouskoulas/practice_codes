def count_sum_k(nums, target):

    prefix_sum = 0
    count = 0 
    pref_freq = {0:1} 

    for num in nums:
        prefix_sum += num 
        complement = prefix_sum - target
        if complement in pref_freq:
            count += pref_freq[complement]
        pref_freq[prefix_sum] = pref_freq.get(num,0) + 1 

    return count


def divisible_by_k(nums, target):

    prefix_sum = 0
    count = 0
    pref_freq = {0:1}

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % target 
        count += pref_freq.get(remainder,0)
        pref_freq[remainder] = pref_freq.get(num,0) + 1 

    return count


def pair_divisible_k(nums,k): 

    seen = set() 

    for num in nums:
        remainder = num % k 
        complement = (k - remainder) % k
        if complement in seen:
            return True
        seen.add(remainder)
    return False



def longest_consec_seq(nums):

    num_set = set(nums)
    max_len = 0 

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1 
            while current + 1 in num_set:
                current += 1 
                length += 1

            max_len = max(length, max_len)

    return max_len

def boyer_moore(nums):

    candidate = None
    count = 0

    # Pass 1: find candidate
    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    # Pass 2: verify candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate

    return None



def balance_eqn(lst):

    balance = 0 

    for item in lst:
        if item == 'START':
            balance += 1 
        elif item == 'STOP':
            balance -= 1 

        if balance < 0:
            return False

    return balance == 0

def elements_with_freq_eql_or_grtr_n_ascending_order_by_element(nums, n):


    from collections import defaultdict

    frequency_pairs = defaultdict(int)

    for num in nums:
        frequency_pairs[num] += 1 

    pair_list = [(x, y) for x, y in frequency_pairs.items()]
    pair_list.sort(key = lambda x: -x[1])

    pairs = [pair for pair in pair_list if pair[1] >= n ]
 
    pairs.sort(key = lambda x: x[0]) #BE CAREFUL BECUAESE THIS RETURNS NONE (modifies in place)

    return pairs


def max_prod_subarry(nums):

    min_prod = global_max = max_prod = nums[0]

    for num in nums[1:]:
        candidates = (num, max_prod * num, min_prod * num)
        min_prod = min(candidates)
        max_prod = max(candidates)
        global_max = max(global_max, max_prod)

    return global_max



def remove_duplicates(nums): 

    left = 0 

    for right in range(1,len(nums)):
        if nums[right] != nums[left]:
            left += 1 
            nums[left]  = nums[right]

    return nums[:left + 1 ]


def move_zeros(nums):

    left = 0 

    for right in range(0, len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 
    return nums


def longest_wo_repeating(chars):

    seen = {}
    left = 0
    longest = float('-inf')


    for right, char in enumerate(chars):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1 
        seen[char] = right
        longest = max(longest, right - left + 1 )

    return longest 


def group_anagrams(words):

    from collections import defaultdict

    anagram_grp = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        anagram_grp[key].append(word)

    return dict(anagram_grp)



class Probability:
    def __init__(self, p_A, p_B = None, p_A_and_B = None, p_A_or_B = None, independent = False):
        self.p_A = p_A
        self.p_B = p_B
        self.p_A_and_B = p_A_and_B
        self.p_A_or_B = p_A_or_B
        self.independent = independent

    def calc_complement_p_A(self):
        return 1 - self.p_A

    def calc_complement_p_B(self):
        return 1 - self.p_B 

    def calc_intersection(self, p_B = None, p_A_and_B = None, p_A_or_B = None, independent = None):

        if p_B is not None:
            self.p_B = p_B

        if p_A_and_B is not None:
            self.p_A_and_B = p_A_and_B

        if p_A_or_B is not None:
            self.p_A_or_B = p_A_or_B

        if independent is None:
            independent = self.independent

        if independent:
            if self.p_B is None:
                raise ValueError("p_B is required when events are independent.")
            return self.p_A * self.p_B

        if self.p_A_and_B is not None:
            return self.p_A_and_B

        if self.p_A_or_B is not None and self.p_B is not None:
            return self.p_A + self.p_B - self.p_A_or_B

        raise ValueError("Insufficient information to compute the intersection.")

    def calc_union(self, p_B = None, p_A_and_B = None, p_A_or_B = None, independent = None):

        if p_B is not None:
            self.p_B = p_B

        if p_A_and_B is not None:
            self.p_A_and_B = p_A_and_B

        if p_A_or_B is not None:
            self.p_A_or_B = p_A_or_B

        if independent is None:
            independent = self.independent

        if self.p_A_or_B is not None:
            return self.p_A_or_B

        if self.p_B is None:
            raise ValueError("p_B is required to compute the union.")

        if independent:
            return self.p_A + self.p_B - (self.p_A * self.p_B)

        if self.p_A_and_B is not None:
            return self.p_A + self.p_B - self.p_A_and_B

        intersection = self.calc_intersection(p_B=self.p_B, independent=False)
        return self.p_A + self.p_B - intersection

