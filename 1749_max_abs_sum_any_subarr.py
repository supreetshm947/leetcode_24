from typing import List

def maxAbsoluteSum(nums: List[int]) -> int:
    max_sum=0
    min_sum=0
    curr_min=0
    curr_max=0

    for num in nums:
        curr_max = max(0, curr_max+num)
        max_sum = max(max_sum, curr_max)

        curr_min = min(0, curr_min+num)
        min_sum = min(min_sum, curr_min)

    return max(max_sum, abs(min_sum))

nums = [2,-5,1,-4,3,-2]
print(maxAbsoluteSum(nums))


