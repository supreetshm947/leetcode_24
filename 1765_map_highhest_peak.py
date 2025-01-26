from typing import List
from collections import deque

def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    m = len(isWater)
    n = len(isWater[0])

    q = deque()
    height = [[-1]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if isWater[i][j]:
                q.append((i, j))
                height[i][j]=0
    
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while(q):
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and height[nx][ny]==-1:
                height[nx][ny]=height[x][y]+1
                q.append((nx, ny))

    return height

isWater = [[0,0,1],[1,0,0],[0,0,0]]
print(highestPeak(isWater))
