from collections import defaultdict, deque
from typing import List

def magnificentSets(n: int, edges: List[List[int]]) -> int:
    def _is_bipartite(node):
        for neighbor in adjacency_list[node]:
            if colors[neighbor] == colors[node]:
                return False
            if colors[neighbor] != -1:
                continue
            colors[neighbor] = (colors[node] + 1) % 2
            if not _is_bipartite(neighbor):
                return False
        return True

    def _find_longest_short_path(node):
        visited = [False]*n
        visited[node] = True
        distance = 0
        q = deque([node])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in adjacency_list[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)
            distance += 1
        return distance

    def _get_number_of_gp_for_component(node, visited):
        visited[node] = True
        max_number_gp = distances[node]

        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                max_number_gp = max(_get_number_of_gp_for_component(neighbor, visited), max_number_gp)
        return max_number_gp

    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u - 1].append(v - 1)
        adjacency_list[v - 1].append(u - 1)

    colors = [-1] * n

    for node in range(n):
        if colors[node] != -1:
            continue
        colors[node] = 0
        if not _is_bipartite(node):
            return -1

    distances = [_find_longest_short_path(node) for node in range(n)]

    visited = [False]*n
    max_number_gp = 0

    for node in range(n):
        if not visited[node]:
            max_number_gp+=_get_number_of_gp_for_component(node, visited)

    return max_number_gp



n = 6
edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
print(magnificentSets(n, edges))
