from typing import List


def maxAscendingSum(nums: List[int]) -> int:
    j=0
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            nums[j] += nums[i]
        else:
            j = i
    return max(nums)

nums = [10,20,30,5,10,50]
print(maxAscendingSum(nums))