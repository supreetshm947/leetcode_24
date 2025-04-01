from typing import List

def minCapability(nums: List[int], k: int) -> int:
        def _can_be_robbed(cap):
            count=0
            i=0
            while i<n:
                if nums[i]<=cap:
                    count+=1
                    i+=1
                i+=1
                if count==k:
                    return True
            return False


        left=min(nums)
        right=max(nums)
        n=len(nums)

        while left<right:
            mid = (left+right)//2
            if _can_be_robbed(mid):
                right=mid
            else:
                left=mid+1

        return left


nums = [2,7,9,3,1]
k = 2

print(minCapability(nums, k))