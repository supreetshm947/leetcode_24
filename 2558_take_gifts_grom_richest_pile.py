from typing import List
import heapq

def pickGifts(gifts: List[int], k: int) -> int:
    gifts = [-gift for gift in gifts]
    heapq.heapify(gifts)
    for i in range(k):
        pile = -heapq.heappop(gifts)
        heapq.heappush(gifts, -int(pile**0.5))
    return -sum(gifts)

gifts = [1,1,1,1]
k = 4
print(pickGifts(gifts, k))
