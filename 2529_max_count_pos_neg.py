from typing import List
import bisect

def maximumCount(nums: List[int]) -> int:
    neg_count = bisect.bisect_left(nums, 0)
    pos_count = bisect.bisect_right(nums, 0)
    return max(neg_count, len(nums)-pos_count)
nums = [-3,-2,-1,0,0,1,2]
print(maximumCount(nums))