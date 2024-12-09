from typing import List
from bisect import bisect_left

def maxTwoEvents(events: List[List[int]]) -> int:
    n = len(events)
    events.sort(key=lambda x: x[1])  # Sort by endTime
    prefix = [0] * n
    prefix[0] = events[0][2]

    # Build prefix max
    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], events[i][2])

    def find_overlapping_index(start_time):
        end_times = [event[1] for event in events]
        index = bisect_left(end_times, start_time)
        return index - 1 if index > 0 else -1

    max_sum = 0
    for i in range(n):
        val = events[i][2]
        index = find_overlapping_index(events[i][0])
        if index != -1:
            val += prefix[index]
        max_sum = max(max_sum, val)

    return max_sum


events = [[1,3,2],[4,5,2],[2,4,3]]
print(maxTwoEvents(events))