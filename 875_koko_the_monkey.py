from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    l=1
    r=max(piles)
    def check(m):
        s=0
        for p in piles:
            s+=(p+m-1)//m
        return s<=h
    while l <= r:
        m=(l+r)//2
        if check(m):
            r=m-1
        else:
            l=m+1
    return l
piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h))