from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:
    n = len(nums)
    memo = {}

    def backtrack(index, curr_sum):
        if index==n:
            return 1 if curr_sum==target else 0
        if (index, curr_sum) in memo:
            return memo[(index, curr_sum)]

        add = backtrack(index + 1, curr_sum + nums[index])
        subtract = backtrack(index + 1, curr_sum - nums[index])

        memo[(index, curr_sum)] = add + subtract
        return memo[(index, curr_sum)]
    return backtrack(0, 0)


nums = [1]
target = 0
print(findTargetSumWays(nums, target))