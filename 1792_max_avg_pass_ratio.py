from typing import List
import heapq

def maxAverageRatio(classes: List[List[int]], extraStudents: int) -> float:
    def calc_change(p, t):
        return (p+1)/(t+1)-p/t

    my_heap = []
    for p, t in classes:
        heapq.heappush(my_heap, (-calc_change(p, t), p, t))

    for _ in range(extraStudents):
        change, p, t = heapq.heappop(my_heap)
        heapq.heappush(my_heap, (-calc_change(p+1, t+1), p+1, t+1))

    total=0
    for _, p, t in my_heap:
        total+=p/t

    return total/len(classes)

classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
print(maxAverageRatio(classes, extraStudents))