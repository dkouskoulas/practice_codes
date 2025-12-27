# Greedy Algorithm - Activity Selection
# Time Complexity: O(n log n) - dominated by sorting
# Space Complexity: O(n) - stores selected activities

# given n activities, each activity has a start and end time 
# can only do one activity at a time
# choose maximum number of activities you can perform such that no two activites overlap ... 
# return maximum number of activites and the list of start/finish times for valid activities


def activities_sort(activities_list):
    
    activities_list.sort(key = lambda x: x[1])

    last_finish = float('-inf')
    count = 0
    activities = []

    for start, finish in activities_list:
        if start >= last_finish:
            activities.append([start,finish])
            count+=1
            last_finish = finish


    return count, activities

