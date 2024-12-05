from typing import DefaultDict
def validArrangement(pairs):
    """
    :type pairs: List[List[int]]
    :rtype: List[List[int]]
    """
    graph, inOutDegree = DefaultDict(list), DefaultDict(int)
    for i, o in pairs:
        graph[i].append(o)
        inOutDegree[i] += 1
        inOutDegree[o] -= 1

    start = pairs[0][0]
    for i in inOutDegree:
        if inOutDegree[i] == 1:
            start=i
            break

    path = []

    def dfs(start):
        while graph[start]:
            n = graph[start].pop()
            path.append((start, n))
            dfs(n)
    dfs(start)
    return path

pairs = [[1,2],[1,3],[2,1]]
print(validArrangement(pairs))