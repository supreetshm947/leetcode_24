from collections import defaultdict
from typing import List

def maximumSum(nums: List[int]) -> int:
    def digit_sum(num):
        out = 0
        while num:
            out+=num%10
            num=num//10
        return out

    digit_sum_map = defaultdict(list)
    nums.sort()

    for num in nums:
        digit_sum_map[digit_sum(num)].append(num)

    max_sum = -1
    for digit_sum in digit_sum_map:
        if len(digit_sum_map[digit_sum]) > 1:
            max_sum = max(max_sum, sum(digit_sum_map[digit_sum][-2:]))

    return max_sum

nums = [10,12,19,14]
print(maximumSum(nums))