from typing import List
from collections import Counter

def divideArray(nums: List[int]) -> bool:
    counter = Counter(nums)
    for val in counter.values():
        if not val % 2 == 0:
            return False
    return True

nums = [1,2,3,4]
print(divideArray(nums))