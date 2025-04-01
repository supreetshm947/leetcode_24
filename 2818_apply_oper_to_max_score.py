from typing import List

def maximumScore(nums: List[int], k: int) -> int:
    MOD = 10**9 + 7
    max_elem = max(nums)

    prime_scores = [0]*(max_elem+1)

    for i in range(2, max_elem+1):
        if prime_scores[i]==0:
            for j in range(i, max_elem+1, i):
                prime_scores[j]+=1

    elem = []
    for i,num in enumerate(nums):
        elem.append((prime_scores[num], i, num))

    elem.sort(key = lambda x: (-x[0], x[1]))

    result = 1
    for i in range(min(k, len(nums))):
        result = (result*elem[i][-1]%MOD)

    return result


nums = [8,3,9,3,8]
k = 2

print(maximumScore(nums, k))