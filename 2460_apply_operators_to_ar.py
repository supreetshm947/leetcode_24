from typing import List

def applyOperations(nums: List[int]) -> List[int]:
    n = len(nums)
    non_zero_index = 0

    for i in range(n-1):
        if nums[i]:
            if nums[i]==nums[i+1]:
                nums[i], nums[i+1] = nums[i+1]*2, 0
            if non_zero_index!=i:
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
            non_zero_index += 1
    if non_zero_index!=n-1:
        nums[n-1], nums[non_zero_index] = nums[non_zero_index], nums[n-1]

    return nums

nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
print(applyOperations(nums))