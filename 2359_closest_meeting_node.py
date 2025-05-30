from collections import deque
from typing import List

def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    if node1==node2:
        return node1

    n = len(edges)

    def _bfs(node):
        distances = [float("inf")]*n
        distances[node] = 0
        q = deque([node])
        visited = {node}
        while q:
            node = q.popleft()
            neighbor = edges[node]
            if neighbor!=-1 and not neighbor in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[node] + 1
                q.append(neighbor)
        return distances

    distances1 = _bfs(node1)
    distances2 = _bfs(node2)

    min_distance_now = float("inf")
    min_distance_node = -1

    for i in range(n):
        max_distance = max(distances1[i], distances2[i])
        if max_distance < min_distance_now:
            min_distance_node=i
            min_distance_now = min(min_distance_now, max(distances1[i], distances2[i]))

    return min_distance_node


edges = [5,3,1,0,2,4,5]
node1 = 3
node2 = 2

print(closestMeetingNode(edges, node1, node2))