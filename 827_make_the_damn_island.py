from typing import List

def largestIsland(grid: List[List[int]]) -> int:

    def _explore_island(x, y):
        if 0<=x<m and 0<=y<n and visited[x][y]==-1  and grid[x][y]==1:
            visited[x][y]=island_id
            return 1 + (
                _explore_island(x-1, y) +
                _explore_island(x, y-1) +
                _explore_island(x+1, y) +
                _explore_island(x, y+1)
            )
        return 0

    m = len(grid)
    n = len(grid[0])
    island_id = 0
    island_sizes = {}

    visited = [[-1] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            size = _explore_island(i, j)
            if size:
                island_sizes[island_id] = size
                island_id += 1

    if not len(island_sizes):
        return 1

    if len(island_sizes) == 1:
        island_size = island_sizes[0]
        return island_size if island_size == m*n else island_size+1

    max_island_size = 0

    for i in range(m):
        for j in range(n):
            if not grid[i][j]:
                current_island_size = 1
                island_set = set()

                if 0<=i-1<m and grid[i-1][j]==1:
                    current_island_size+=island_sizes[visited[i-1][j]]
                    island_set.add(visited[i-1][j])

                if 0 <= i + 1 < m and grid[i + 1][j] == 1 and visited[i+1][j] not in island_set:
                    current_island_size+=island_sizes[visited[i+1][j]]
                    island_set.add(visited[i+1][j])

                if 0 <= j-1 < n and grid[i][j-1] == 1 and visited[i][j-1] not in island_set:
                    current_island_size+=island_sizes[visited[i][j-1]]
                    island_set.add(visited[i][j-1])

                if 0<=j+1 < n and grid[i][j+1] == 1 and visited[i][j+1] not in island_set:
                    current_island_size+=island_sizes[visited[i][j+1]]

                max_island_size = max(max_island_size, current_island_size)

    return max_island_size

grid = [[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]]
print(largestIsland(grid))