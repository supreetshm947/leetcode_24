from typing import List

def countServers(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    row_count = [0]*m
    col_count = [0]*n

    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                row_count[i]+=1
                col_count[j]+=1


    total=0
    for i in range(m):
        for j in range(n):
            if grid[i][j] and (row_count[i]>1 or col_count[j]>1):
                total+=1

    return total

grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
print(countServers(grid))