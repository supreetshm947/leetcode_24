from collections import deque

def minimumRecolors(blocks: str, k: int) -> int:
    q = deque(maxlen=k)
    num_white = 0
    for i in range(k):
        if blocks[i] == "W":
            num_white+=1
        q.append(blocks[i])

    min_white = num_white

    for i in range(k, len(blocks)):
        if q.popleft() == "W":
            num_white-=1

        if blocks[i] == "W":
            num_white+=1
        q.append(blocks[i])

        min_white = min(num_white, min_white)

    return min_white

blocks = "WBWBBBW"
k = 2
print(minimumRecolors(blocks, k))