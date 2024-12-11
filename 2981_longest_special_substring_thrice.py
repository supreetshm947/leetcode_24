from collections import defaultdict
def maximumLength(s: str) -> int:
    i, j = 0, 0
    n = len(s)
    comb = defaultdict(int)
    while i < n:
        if j == n or s[i] != s[j]:
            i += 1
            j = i
            continue
        comb[s[i:j + 1]] += 1
        j += 1
    max_len = -1
    for k, v in comb.items():
        if v>=3:
            max_len = max(max_len, len(k))
    return max_len
s = "abcdef"
print(maximumLength(s))
