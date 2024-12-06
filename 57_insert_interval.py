from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    merged = []
    n = len(intervals)
    i = 0
    if not intervals:
        return [newInterval]
    while i < n and newInterval[0] >= intervals[i][1]:
        merged.append(intervals[i])
        i += 1
    newInterval[0] = min(newInterval[0], intervals[i][0])

    while i < n and newInterval[1] >= intervals[i][0]:
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    merged.append(newInterval)
    while i < n:
        merged.append(intervals[i])
        i += 1
    return merged

intervals =  [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))