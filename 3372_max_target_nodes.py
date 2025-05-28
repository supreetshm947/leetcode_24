from collections import defaultdict
from typing import List

def maxTargetNodes(edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
    def dfs(node, parent, children, k)->int:
        if k<0:
            return 0
        result = 1
        for child in children[node]:
            if child != parent:
                result += dfs(child, node, children, k-1)
        return result

    def build_count(edges: List[List[int]], k) -> List[int]:
        children = defaultdict(list)
        for edge in edges:
            children[edge[0]].append(edge[1])
            children[edge[1]].append(edge[0])
        count = [0] * (len(edges) + 1)
        for node in range(len(edges) + 1):
            count[node] = dfs(node, None, children, k)
        return count

    count1 = build_count(edges1, k)
    count2 = build_count(edges2, k-1)

    max_len2 = max(count2)
    out = [max_len2+i for i in count1]

    return out


edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
k = 2
print(maxTargetNodes(edges1, edges2, k))
