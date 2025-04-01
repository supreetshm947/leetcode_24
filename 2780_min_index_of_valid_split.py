from typing import List

def minimumIndex(nums: List[int]) -> int:
    candidate, count = None, 0
    for num in nums:
        if not count:
            candidate = num
        count += 1 if candidate == num else -1

    count = sum(1 for num in nums if num == candidate)

    left_count=0
    n = len(nums)
    for i in range(n-1):
        if nums[i] == candidate:
            left_count += 1
        left_size = i+1
        right_size = n - left_size
        right_count = count-left_count

        if left_count * 2 > left_size and right_count * 2 > right_size:
            return i

    return -1

nums = [1,2,2,2]
print(minimumIndex(nums))