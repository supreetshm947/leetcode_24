from typing import List

def check(nums: List[int]) -> bool:
    inversion=0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            inversion+=1
    if nums[-1]>nums[0]:
        inversion+=1
    return inversion<=1

nums = [1,2,3]
print(check(nums))