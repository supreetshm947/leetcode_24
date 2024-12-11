from typing import List

def search(nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[left] < nums[mid]:
            if target in nums[left:mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target in nums[mid+1:right+1]:
                left = mid + 1
            else:
                right = mid - 1
    return False
nums = [1,0,1,1,1]
#[2,5,6,0,0,1,2]
for num in nums:
    print(search(nums, num))
target = 3
print(search(nums, target))