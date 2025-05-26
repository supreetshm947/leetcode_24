from typing import List
from collections import defaultdict, deque

def largestPathValue(colors: str, edges: List[List[int]]) -> int:
    n = len(colors)
    dp = [[0] * 26 for _ in range(n)]

    adjacency_list = defaultdict(list)
    in_degree = [0] * n
    for current, v in edges:
        adjacency_list[current].append(v)
        in_degree[v] += 1

    q = deque()
    for k in range(n):
        dp[k][ord(colors[k]) - ord('a')] = 1
        if in_degree[k] == 0:
            q.append(k)

    visited = 0

    while q:
        current = q.popleft()
        for neighbor in adjacency_list[current]:
            for c in range(26):
                add = 1 if c == ord(colors[neighbor]) - ord('a') else 0
                dp[neighbor][c] = max(dp[neighbor][c], dp[current][c] + add)
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)
        visited += 1

    if visited < n:
        return -1

    return max(max(row) for row in dp)


colors = "spppsssss"
edges = [[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[5,6],[6,7],[5,7],[1,8]]
print(largestPathValue(colors, edges))
