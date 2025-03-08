from typing import List

def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    n = len(grid)
    size = n*n
    exists = [0]*(size+1)

    for i in range(n):
        for j in range(n):
            exists[grid[i][j]] += 1

    pos_a=-1
    pos_b=-1

    for i in range(1, size+1):
        if exists[i] == 2:
            pos_a = i
        if not exists[i]:
            pos_b = i

    return [pos_a, pos_b]

grid = [[1,3],[2,2]]
print(findMissingAndRepeatedValues(grid))