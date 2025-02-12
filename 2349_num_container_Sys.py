import heapq
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.index_to_num = defaultdict(int)
        self.num_to_index = defaultdict(list)
    def change(self, index: int, number: int) -> None:
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_index[number], index)
    def find(self, number: int) -> int:
        if number not in self.index_to_num.values():
            return -1
        while self.num_to_index[number]:
            t = self.num_to_index[number][0]
            if self.index_to_num[t]!=number:
                heapq.heappop(self.num_to_index[number])
            else:
                return t
        return -1

obj = NumberContainers()

print(obj.find(10))
print(obj.change(2, 10))
print(obj.change(1, 10))
print(obj.change(3, 10))
print(obj.change(5, 10))
print(obj.find(10))
print(obj.change(1, 20))
print(obj.find(10))

