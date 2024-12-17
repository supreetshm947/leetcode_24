from typing import List

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid +1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right=right-1

    return nums[left]

nums = [2,2,0,1]
print(findMin(nums))