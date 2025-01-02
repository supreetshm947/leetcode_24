from typing import List

def mincostTickets(days: List[int], costs: List[int]) -> int:
    n=len(days)
    dp = [0]*(days[n-1]+1)

    i=0
    for day in range(days[n-1]+1):
        if day<days[i]:
            dp[day]=dp[day-1]
        else:
            i+=1
            dp[day]=min(dp[day-1]+costs[0],
                        dp[max(0, day-7)]+costs[1],
                        dp[max(0, day-30)]+costs[2])
    return dp[-1]

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2, 7, 15]
print(mincostTickets(days, costs))