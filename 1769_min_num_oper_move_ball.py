from typing import List

def minOperations(boxes: str) -> List[int]:
    n=len(boxes)
    ans = [0]*n

    count=0
    operations=0

    for i in range(n):
        operations+=count
        ans[i]=operations
        count+=int(boxes[i])

    count=0
    operations=0

    for i in range(n-1, -1, -1):
        operations += count
        ans[i]+=operations
        count+=int(boxes[i])

    return ans

boxes = "110"
print(minOperations(boxes))