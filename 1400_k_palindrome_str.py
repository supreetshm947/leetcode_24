from collections import defaultdict

def canConstruct(s: str, k: int) -> bool:
    n = len(s)
    if n < k:
        return False
    if n == k:
        return True
    d = defaultdict(int)
    for c in s:
        d[c]+=1
    odd = 0
    for v in d.values():
        if v % 2 == 1:
            odd+=1
    return odd<=k


s = "true"
k = 4
print(canConstruct(s, k))