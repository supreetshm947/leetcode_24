import heapq

def minimumObstacles(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])

    moves = [(-1,0), (0,-1), (1,0), (0,1)]
    q = [(0,0,0)]
    visited = [[float("inf")]*n for _ in range(m)]

    visited[0][0] = 0

    while q:
        cost, i, j = heapq.heappop(q)
        if i==m-1 and j==n-1:
            return cost
        for dx, dy in moves:
            x, y = i+dx, j+dy
            if 0<=x<m and 0<=y<n:
                curr_cost = cost+grid[x][y]
                if curr_cost < visited[x][y]:
                    visited[x][y] = curr_cost
                    heapq.heappush(q, (curr_cost, x, y))

grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
print(minimumObstacles(grid))