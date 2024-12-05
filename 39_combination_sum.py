def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def backtrack(start, sum, comb):
        if sum == target:
            result.append(comb)
            return
        for i in range(start, len(candidates)):
            if sum + candidates[i] > target:
                continue
            backtrack(i, sum + candidates[i], comb + [candidates[i]])

    result = []
    backtrack(0, 0, [])
    return result

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))