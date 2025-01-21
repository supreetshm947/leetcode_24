from typing import List
import heapq

def trapRainWater(heightMap: List[List[int]]) -> int:
    m = len(heightMap)
    n = len(heightMap[0])

    visited = [[False] * n for _ in range(m)]

    heap = []
    water_trapped = 0

    for i in range(m):
        for j in range(n):
            if i==0 or i==m-1 or j==0 or j==n-1:
                visited[i][j] = True
                heapq.heappush(heap, (heightMap[i][j], i, j))

    direction = [(0,1), (0,-1), (-1,0), (1,0)]

    while heap:
        height, i, j = heapq.heappop(heap)
        for dx, dy in direction:
            nx, ny = i + dx, j + dy
            if 0<nx<m-1 and 0<ny<n-1 and not visited[nx][ny]:
                visited[nx][ny] = True
                water_trapped += max(0, height-heightMap[nx][ny])
                heapq.heappush(heap, (max(heightMap[nx][ny], height), nx, ny))

    return water_trapped

heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
print(trapRainWater(heightMap))