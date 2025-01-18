from typing import List

def doesValidArrayExist(derived: List[int]) -> bool:
    xor = 0
    for i in derived:
        xor ^= i
    return xor == 0

derived = [1,0]
print(doesValidArrayExist(derived))