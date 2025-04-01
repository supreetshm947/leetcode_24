from typing import List

def countDays(days: int, meetings: List[List[int]]) -> int:
    latest_end = 0
    free_day = 0

    meetings.sort()

    for start, end in meetings:
        if start > latest_end+1:
            free_day += start-latest_end-1

        latest_end = max(latest_end, end)

    return free_day+(days-latest_end)

days =6
meetings = [[1,6]]
print(countDays(days, meetings))