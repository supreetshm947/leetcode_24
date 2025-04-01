from typing import List

def longestNiceSubarray(nums: List[int]) -> int:
    left=0
    max_len = 0
    bitmask = 0

    for i in range(len(nums)):
        while bitmask & nums[i] !=0:
            bitmask &= ~nums[left]
            left += 1

        bitmask |= nums[i]
        max_len = max(max_len, i - left + 1)

    return max_len


nums = [3,1,5,11,13]
print(longestNiceSubarray(nums))