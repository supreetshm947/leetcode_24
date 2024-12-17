import heapq
from typing import List

def findScore(nums: List[int]) -> int:
    marked = [False] * len(nums)
    score = 0
    min_heap = []
    for i,v in enumerate(nums):
        heapq.heappush(min_heap, (v, i))
    while min_heap:
        num, i = heapq.heappop(min_heap)
        if marked[i]:
            continue
        score += num
        marked[i] = True
        if i>0:
            marked[i-1] = True
        if i+1<len(nums):
            marked[i+1] = True

    return score


nums = [2,1,3,4,5,2]
print(findScore(nums))