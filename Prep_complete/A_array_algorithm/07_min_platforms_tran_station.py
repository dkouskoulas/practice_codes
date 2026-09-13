"""

Given two arrays arr[] and dep[], that represent the arrival and departure time of i-th train 
respectively. Find the minimum number of platforms required so that no train has to wait. 
If the departure time of one train is the same as the arrival time of another train, 
both trains cannot use the same platform at that time.
"""

def meeting_rooms(arr, dep):

    if len(arr) != len(dep):
        raise ValueError("Length mismatch!")

    arrivals = sorted(arr)
    departures = sorted(dep)

    arr, dep = 0, 0
    platforms, max_platforms = 0, 0

    while arr < len(arrivals):
        if arrivals[arr] < departures[dep]:
            platforms += 1 
            max_platforms = max(platforms, max_platforms)
            arr += 1
        else:
            platforms -= 1 
            dep += 1 

    return max_platforms