from typing import List
def minimumSize(nums: List[int], maxOperations: int) -> int:
    def can_split(mid):
        num_splits = 0
        for ball in nums:
            if ball > mid:
                num_splits += (ball-1) // mid
        return num_splits <= maxOperations

    left, right = 1, max(nums)
    while left < right:
        mid = (right + left) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid+1
    return left
nums = [2,4,8,2]
maxOperations = 2
print(minimumSize(nums, maxOperations))