# Two Pointers - Container With Most Water
# Time Complexity: O(n) - single pass with two pointers
# Space Complexity: O(1) - only uses constant extra space



def max_area(height):

    left, right = 0, len(height) - 1
    max_water = 0 

    while left < right:

        width = right - left 

        current_height = min(height[left], height[right])
        current_area = width * current_height

        max_water = max(max_water, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water