from typing import List
from collections import defaultdict, deque


def countCompleteComponents(n: int, edges: List[List[int]]) -> int:
    adjacency_list = defaultdict(set)

    for u, v in edges:
        adjacency_list[u].add(v)
        adjacency_list[v].add(u)

    visited = set()
    complete_count = 0

    def bfs(start):
        queue = deque([start])
        visited.add(start)
        component_nodes = {start}
        edge_count = 0

        while queue:
            node = queue.popleft()
            for neighbor in adjacency_list[node]:
                edge_count += 1  # Count each edge
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    component_nodes.add(neighbor)

        k = len(component_nodes)
        return edge_count // 2 == (k * (k - 1)) // 2

    for i in range(n):
        if i not in visited:
            if bfs(i):
                complete_count += 1

    return complete_count




n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
print(countCompleteComponents(n, edges))