from typing import List

def isArraySpecial(nums: List[int]) -> bool:
    for i in range(len(nums)-1):
        if not nums[i]&1 ^ nums[i+1]&1:
            return False
    return True

nums = [4,3,1,6]
print(isArraySpecial(nums))