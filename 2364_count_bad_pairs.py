from typing import List

def countBadPairs(nums: List[int]) -> int:
    diff_map = {}
    out=0
    for i in range(len(nums)):
        diff=i-nums[i]
        good_pairs =diff_map.get(diff, 0)
        out +=i-good_pairs
        diff_map[diff]=good_pairs+1
    return out

nums = [4,1,3,3]
print(countBadPairs(nums))