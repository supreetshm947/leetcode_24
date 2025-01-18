from typing import List

def combinatonSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    n=len(candidates)
    def backtrack(sum, curr_list, i):
        if sum == target:
            res.append(curr_list[:])
            return
        if sum>target:
            return
        for j in range(i,n):
            if j > i and candidates[j] == candidates[j - 1]:
                continue

            curr_list.append(candidates[j])
            backtrack(sum + candidates[j], curr_list, j + 1)
            curr_list.pop()
    backtrack(0, [], 0)
    return res


# Todo fix dupolicates
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinatonSum2(candidates, target))