from typing import List
from collections import defaultdict

def maxKDivisibleComponents(n: int, edges: List[List[int]], values: List[int], k: int) -> int:
    visited = [False]*n
    out = 0

    edge_map = defaultdict(list)
    for i,j in edges:
        edge_map[i].append(j)
        edge_map[j].append(i)

    def dfs(node):
        nonlocal out
        visited[node] = True
        s=values[node]
        for neighbor in edge_map[node]:
            if not visited[neighbor]:
                s+=dfs(neighbor)
        if s%k==0:
            out+=1
            return 0
        return s

    dfs(0)
    return out


n = 7
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
values = [3, 0, 6, 1, 5, 2, 1]
k = 3

print(maxKDivisibleComponents(n, edges, values, k))




