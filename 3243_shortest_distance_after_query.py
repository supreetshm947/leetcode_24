from collections import deque

def shortestDistanceAfterQueries(n, queries):
    """
    :type n: int
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    graph = dict()
    for i in range(n):
        graph[i] = [i+1]

    def bfs():
        q = deque([[0,0]])
        visited = set()
        while q:
            node, distance = q.popleft()

            if node == n-1:
                return distance
            if node in visited:
                continue
            visited.add(node)
            for neighbour in graph[node]:
                q.append([neighbour, distance+1])

    shortest_distance = []
    for l, r in queries:
        graph[l].append(r)
        shortest_distance.append(bfs())
    return shortest_distance

n =5
queries =[[2,4],[0,2],[0,4]]

print(shortestDistanceAfterQueries(n,queries))