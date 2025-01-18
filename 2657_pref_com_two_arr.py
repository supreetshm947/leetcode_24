from typing import List
from collections import defaultdict

def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    n = len(A)
    freq = defaultdict(int)
    comm_count = 0
    out = []
    for i in range(n):
        freq[A[i]] += 1
        if freq[A[i]] == 2:
            comm_count += 1
        freq[B[i]] += 1
        if freq[B[i]] == 2:
            comm_count += 1
        out.append(comm_count)
    return out

A = [2,3,1]
B = [3, 1, 2]

print(findThePrefixCommonArray(A, B))
