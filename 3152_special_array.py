from typing import List

def isArraySpecial(nums: List[int], queries: List[List[int]]) -> List[bool]:
    n = len(nums)
    group_ar = [0] * n
    curr_group = 0

    for i in range(1, n):
        if nums[i] % 2 == nums[i - 1] % 2:
            curr_group += 1
        group_ar[i]=curr_group
    m = len(queries)
    out = [False] * m
    for i in range(m):
        out[i] = group_ar[queries[i][0]] == group_ar[queries[i][1]]

    return out

nums = [4,3,1,6]
queries = [[0,2],[2,3]]
print(isArraySpecial(nums, queries))