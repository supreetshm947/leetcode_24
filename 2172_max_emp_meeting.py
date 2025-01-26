from typing import List
from collections import deque, defaultdict

def maximumInvitations(favorite: List[int]) -> int:
    def _bfs(start_node, visited_nodes):
        q = deque([(start_node, 0)])
        max_len = 0
        while q:
            n, d = q.popleft()
            for neighbor in reversed_graph[n]:
                if neighbor in visited_nodes:
                   continue
                visited_nodes.add(neighbor)
                q.append((neighbor, d+1))
                max_len = max(max_len, d + 1)
        return max_len

    n = len(favorite)

    reversed_graph = defaultdict(list)
    visited = [False]*n
    longest_cycle = 0
    two_cycle_invitation = 0

    for i in range(n):
        reversed_graph[favorite[i]].append(i)

    for i in range(n):
        if not visited[i]:
            current_node = i
            visited_persons = {}
            distance = 0
            while True:
                if visited[current_node]:
                    break
                visited[current_node] = True
                visited_persons[current_node] = distance
                distance+=1
                next_person = favorite[current_node]

                if next_person in visited_persons:
                    cycle_len = distance - visited_persons[next_person]
                    longest_cycle = max(longest_cycle, cycle_len)

                    if cycle_len ==2:
                        visited_nodes = {current_node, next_person}

                        two_cycle_invitation += (
                            2 +
                            _bfs(current_node, visited_nodes)
                            + _bfs(next_person, visited_nodes)
                        )
                    break
                current_node = next_person

    return max(longest_cycle, two_cycle_invitation)

favorite = [3,0,1,4,1]
print(maximumInvitations(favorite))