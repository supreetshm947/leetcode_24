import heapq
from typing import List

def minOperations(nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    num_oper=0
    while nums[0]<k:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        t = min(x,y)*2+max(x,y)
        heapq.heappush(nums,t)
        num_oper+=1
    return num_oper

nums = [2,11,10,1,3]
k = 10
print(minOperations(nums, k))