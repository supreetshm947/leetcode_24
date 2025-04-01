from typing import List
import math

def repairCars(ranks: List[int], cars: int) -> int:
    # r*n^2<=T
    def _can_repair(t):
        out = 0
        for i in ranks:
            out+=int(math.sqrt(t//i)) # n<=(T/r)^0.5
            if out>=cars:
                return True
        return False


    left, right = 1, max(ranks)*cars*cars # from 0 to Maximum amount of Time

    while left<right:
        mid = (left + right) // 2
        if _can_repair(mid):
            right=mid
        else:
            left=mid+1

    return left

ranks = [4,2,3,1]
cars = 10
print(repairCars(ranks, cars))