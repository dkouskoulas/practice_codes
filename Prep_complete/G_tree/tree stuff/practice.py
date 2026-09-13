


from collections import deque


def bfs_levels(root):

    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level = []
        size = len(q)

        for _ in range(size):
            node = q.popleft()
            level.append(node.value)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        resut.append(level)

    return result


    def longest_consecutive(nums):

        num_set = set(nums)
        longest = 0

        for num in num_set:

            # check if the number less than current is in set
            if num - 1 not in num_set:

                # if not, reset
                current_num = num
                current_length = 1 

                while current_num + 1 in num_set:
                    current_num += 1 
                    current_length += 1 

                longest  = max(longest, current_num)

        return longest


    def reverse_array(nums):

        left = 0 
        right = len(nums) - 1 

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1 
            right -= 1 

        return nums


    def move_zeros(nums):

        left = 0 

        for right in range(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums


    def remove_duplicates(nums):

        left = 1 

        for right in range(1, len(nums)):

            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1 

        return left 

    def partition_arrays(nums, x):

        left = 0

        for right in range(len(nums)):
            if nums[right] < x:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums


    def subarray_sum(nums, k):

        prefix_count = {0:1}

        current_sum = 0 
        total = 0

        for num in nums:

            current_sum += num

            if current_sum - k in prefix_count:
                total += prefix_count[current_sum - k]

            prefix_count[current_sum] = prefix_count.get(current_sum,0) + 1 
        
        return total


    def majority_element(nums):

        count = 0
        candidate = None


        for num in nums:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1 

            else:
                count -= 1 

        return candidate


