def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i - 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)
        dfs(i + 1, j)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1':
                count += 1
                dfs(i, j)

    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))