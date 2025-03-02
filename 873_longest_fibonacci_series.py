from typing import List

def lenLongestFibSubseq(arr: List[int]) -> int:
    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    val_to_idx = {val:i for i, val in enumerate(arr)}
    max_len = 0

    for curr in range(n):
        for prev in range(curr):
            diff = arr[curr] - arr[prev]
            idx = val_to_idx.get(diff, -1)
            dp[prev][curr] = dp[idx][prev]+1 if 0 <= idx < prev else 2
            max_len = max(max_len, dp[prev][curr])

    return max_len if max_len > 2 else 0

arr = [1,3,7,11,12,14,18]
print(lenLongestFibSubseq(arr))