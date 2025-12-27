# Greedy Algorithm - Maximum Non-Overlapping Intervals
# Time Complexity: O(n log n) - dominated by sorting
# Space Complexity: O(1) - only uses constant extra space

# Given a list of intervals, where each interval has a start time and an end time, 
# choose the maximum number of non-overlapping intervals.

# Return the maximum number of intervals you can select (or the actual set).


def interview_schedular(intervals):

    intervals.sort(key = lambda x: x[1])

    count = 0
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end

    return count