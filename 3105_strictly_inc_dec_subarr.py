from typing import List

def longestMonotonicSubarray(nums: List[int]) -> int:
    inc_len = 1
    dec_len = 1
    max_len = 1
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            inc_len += 1
            dec_len = 1
        elif nums[i] > nums[i+1]:
            dec_len += 1
            inc_len = 1
        else:
            inc_len = dec_len = 1
        max_len = max(inc_len, dec_len, max_len)

    return max_len

nums = [1,10,10]
print(longestMonotonicSubarray(nums))