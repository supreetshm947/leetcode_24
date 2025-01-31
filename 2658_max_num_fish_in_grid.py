from typing import List
from collections import deque

def findMaxFish(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

    visited = [[False] * m for _ in range(n)]
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def _bfs(i, j):
        q = deque([(i, j)])
        out = grid[i][j]
        while q:
            x, y = q.popleft()
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True  
                        if grid[nx][ny] > 0:
                            q.append((nx, ny))
                        out+=grid[nx][ny]
        return out

    max_fish = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                visited[i][j] = True
                if grid[i][j] > 0:
                    max_fish = max(max_fish, _bfs(i, j))

    return max_fish

grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]

print(findMaxFish(grid))