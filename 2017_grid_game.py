from typing import List

def gridGame(grid: List[List[int]]) -> int:
    n = len(grid[0])

    top_prefix = [0]*n
    bottom_prefix = [0]*n

    top_prefix[0] = grid[0][0]
    bottom_prefix[0] = grid[1][0]

    for i in range(1,n):
        top_prefix[i]=top_prefix[i-1]+grid[0][i]
        bottom_prefix[i]=bottom_prefix[i-1]+grid[1][i]

    min_points = float("inf")

    for i in range(n):
        top_points = top_prefix[-1]-top_prefix[i] if i<n-1 else 0
        bottom_points = bottom_prefix[i-1] if i>0 else 0

        max_points = max(top_points, bottom_points)

        min_points = min(min_points, max_points)

    return min_points



grid = [[2,5,4],[1,5,1]]
print(gridGame(grid))
