from typing import List

def continuousSubarrays(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    i, j = 0, 0
    low=nums[0]
    high=nums[0]
    count = 0
    while i < n:
        if j<n and abs(low-nums[j])<=2 and abs(high-nums[j])<=2:
            count+=1
            low=min(low,nums[j])
            high=max(high,nums[j])
            j+=1
        else:
            i+=1
            j=i
            if i<n:
                high=nums[i]
                low=nums[i]
    return count

nums=[1,2,3]
print(continuousSubarrays(nums))