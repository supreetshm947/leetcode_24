from typing import List

def minOperations(nums: List[int]) -> int:
    n = len(nums)
    count = 0
    for i in range(n-2):
        if not nums[i]:
            count+=1
            nums[i:i+3] = [abs(t-1) for t in nums[i:i+3]]

    return -1 if n != sum(nums) else count


nums = [0,1,1,1]
print(minOperations(nums))