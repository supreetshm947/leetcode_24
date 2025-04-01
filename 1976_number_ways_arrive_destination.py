from typing import List
from collections import defaultdict
from heapq import heappop, heappush

def countPaths(n: int, roads: List[List[int]]) -> int:
    MOD = 10 ** 9 + 7

    graph = defaultdict(list)

    for u,v,t in roads:
        graph[u].append((v, t))
        graph[v].append((u, t))

    ways = [0 for i in range(n)]
    ways[0] = 1

    shortest_path = [float('inf') for i in range(n)]
    shortest_path[0] = 0

    heap = [(0,0)] #time, node

    while heap:
        curr_time, curr_node = heappop(heap)

        for u, t in graph[curr_node]:
            new_time = curr_time + t
            if new_time < shortest_path[u]:
                shortest_path[u] = new_time
                ways[u] = ways[curr_node]
                heappush(heap, (new_time, u))

            elif new_time == shortest_path[u]:
                ways[u] = (ways[curr_node]+ways[u])%MOD

    return ways[-1]

n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(countPaths(n,roads))