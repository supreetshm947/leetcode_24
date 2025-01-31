from collections import defaultdict
from typing import List

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    def _is_connected(src, target):
        visited[src] = True
        if src == target:
            return True
        for node in adj[src]:
            if not visited[node]:
                if _is_connected(node, target):
                    return True
        return False

    n = len(edges)
    adj = defaultdict(list)
    for src, target in edges:
        visited = [False]*n
        if _is_connected(src-1, target-1):
            return [src, target]
        adj[src-1].append(target-1)
        adj[target-1].append(src-1)

    return []

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(findRedundantConnection(edges))