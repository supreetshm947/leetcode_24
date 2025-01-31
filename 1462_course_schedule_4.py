from typing import List
from collections import defaultdict

def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    def _bfs(visited, start, target):
        if start == target:
            return True

        for e in adjacency_list[start]:
            if e not in visited:
                visited.append(e)
                if _bfs(visited, e, target):
                    return True
        return False

    adjacency_list =  defaultdict(list)

    for preq in prerequisites:
        adjacency_list[preq[0]].append(preq[1])

    out = []
    for queries in queries:
        visited = []
        out.append(_bfs(visited, queries[0], queries[1]))

    return out

numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]
print(checkIfPrerequisite(numCourses, prerequisites, queries))