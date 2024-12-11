from functools import reduce
from typing import List
def maximumBeauty(nums: List[int], k: int) -> int:
    return nums.sort() or len(nums)-reduce(lambda i,x: i+(x-nums[i]>2*k), nums, 0)
    # return nums.sort() or len(nums) - reduce(lambda l, m: l + (m - nums[l] > 2 * k), nums, 0)

nums = [5,57,46]
k = 15
print(maximumBeauty(nums, k))