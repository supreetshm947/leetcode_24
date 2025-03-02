from collections import defaultdict, deque
from typing import List

def mostProfitablePath( edges: List[List[int]], bob: int, amount: List[int]) -> int:
    def _find_bob_path(curr, time):
        visited[curr] = True
        bob_path[curr] = time

        if curr == 0:
            return True

        for neighbor in adjacency_list[curr]:
            if not visited[neighbor]:
                if _find_bob_path(neighbor, time+1):
                    return True

        bob_path.pop(curr)
        return False


    n = len(amount)
    adjacency_list = defaultdict(list)

    for i, j in edges:
        adjacency_list[i].append(j)
        adjacency_list[j].append(i)

    bob_path = {}
    visited = [0]*n

    _find_bob_path(bob, 0)

    visited = [0] * n
    q = deque([(0,0,0)])
    max_income = float("-inf")

    while q:
        curr, time, profit = q.popleft()
        visited[curr] = True
        # alice reached first
        if curr not in bob_path or bob_path[curr] > time:
            profit+=amount[curr]

        elif time == bob_path[curr]:
            profit+=amount[curr]//2

        if len(adjacency_list[curr])==1 and curr!=0:
            max_income = max(max_income, profit)

        for neighbor in adjacency_list[curr]:
            if not visited[neighbor]:
                q.append((neighbor,time+1,profit))

    return max_income

edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]

print(mostProfitablePath(edges, bob, amount))