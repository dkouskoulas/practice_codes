# Question:
# Given an array of meeting time intervals [[start, end]], 
# determine if a person can attend all meetings (i.e., no overlapping meetings).

def can_attend_meetings(intervals):
    if not intervals:
        return True
    
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True


# Question 2: Meeting Rooms II
# Given an array of meeting time intervals, find the minimum number of conference rooms required.

def min_meeting_rooms(intervals):

    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    start, end = 0, 0
    rooms, max_rooms = 0,0 

    while start < len(starts):
        if starts[start] < ends[end]:
            rooms += 1
            max_rooms = max(rooms, max_rooms)
            start += 1 
        else:
            rooms -= 1 
            end += 1

    return max_rooms
