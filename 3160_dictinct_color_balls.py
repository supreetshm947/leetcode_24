from typing import List
from collections import defaultdict

def queryResults(limit: int, queries: List[List[int]]) -> List[int]:
    color_count = defaultdict(int)
    ball_color = defaultdict(int)
    out = []

    for query in queries:
        ball, color = query
        if prev_color:=ball_color[ball]:
            color_count[prev_color] -= 1
            if not color_count[prev_color]:
                del color_count[prev_color]
        ball_color[ball] = color
        color_count[color] += 1
        out.append(len(color_count))

    return out

limit = 4
queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
print(queryResults(limit, queries))