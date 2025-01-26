from typing import List
from collections import defaultdict

def lexicographicallySmallestArray(nums: List[int], limit: int) -> List[int]:
    n = len(nums)

    nums_sorted = sorted(nums)
    curr_group = 0

    group_to_num, num_to_group = defaultdict(list), defaultdict(int)

    group_to_num[curr_group].append(nums_sorted[0])
    num_to_group[nums_sorted[0]] = curr_group

    for i in range(1, n):
        if nums_sorted[i] - nums_sorted[i-1] > limit:
            curr_group+=1
        group_to_num[curr_group].append(nums_sorted[i])
        num_to_group[nums_sorted[i]] = curr_group

    out = []
    for i in nums:
        out.append(group_to_num[num_to_group[i]].pop(0))

    return out


nums = [1,7,28,19,10]
limit = 3
print(lexicographicallySmallestArray(nums, limit))