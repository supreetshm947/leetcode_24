from typing import List
from collections import deque

def minCost(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    cost = [[float("inf")]*n for _ in range(m)]
    cost[0][0] = 0

    moves = [(0,1), (0, -1), (1, 0), (-1, 0)]

    q = deque([(0,0,0)])

    while q:
        x, y, curr_cost = q.popleft()

        if x == m-1 and y == n-1:
            return cost[x][y]

        for d, (dx, dy) in enumerate(moves, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_cost = curr_cost if grid[x][y]==d else curr_cost+1
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    if grid[x][y]==d:
                        q.appendleft([nx,ny,new_cost])
                    else:
                        q.append([nx,ny,new_cost])

    return cost[m-1][n-1]


grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
print(minCost(grid))