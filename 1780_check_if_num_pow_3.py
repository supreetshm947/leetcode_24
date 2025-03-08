import numpy as np
def checkPowersOfThree(n: int) -> bool:
    return not "2" in np.base_repr(n, 3)

n=12
print(checkPowersOfThree(12))