from typing import List
from collections import defaultdict

def tupleSameProduct(nums: List[int]) -> int:
    prods = {}
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            prod=nums[i]*nums[j]
            if prod not in prods:
                prods[prod] = 1
            else:
                prods[prod]+=1

    out = 0
    for prod in prods.values():
        prod_pairs = (prod-1)*prod//2
        out += prod_pairs*8

    return out


nums = [2,3,4,6,8,12]
print(tupleSameProduct(nums))