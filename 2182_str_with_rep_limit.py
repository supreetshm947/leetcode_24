import heapq
from collections import Counter
def repeatLimitedString(s: str, repeatLimit: int) -> str:
    counter = Counter(s)
    heap = [(-ord(c), c, count) for c, count in counter.items()]
    heapq.heapify(heap)

    out = ""

    while heap:
        o, c, count = heapq.heappop(heap)
        limit = min(count, repeatLimit)
        out += c * limit
        remaining = count - limit
        if remaining > 0 and heap:
            next_o, next_c, next_count = heapq.heappop(heap)
            out += next_c
            if next_count-1>0:
                heapq.heappush(heap, (next_o, next_c, next_count-1))
            heapq.heappush(heap, (o, c, remaining))

    return out

s = "cczazcc"
repeatLimit = 3
print(repeatLimitedString(s, repeatLimit))