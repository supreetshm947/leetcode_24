from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort the array to use two-pointer approach effectively
    n = len(nums)
    out = []

    for i in range(n - 2):  # Iterate through each number
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for the first number
            continue

        left, right = i + 1, n - 1  # Initialize two pointers
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                out.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for `left` and `right`
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
    return out

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
