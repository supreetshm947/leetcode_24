from typing import List

def findMin(nums: List[int]) -> int:
    m=float("inf")
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        m=min(m, nums[mid])
        if nums[left] <= nums[mid]:
            m=min(m, nums[left])
            left=mid+1
        else:
            right=mid-1
    return m
nums = [2,1]
print(findMin(nums))