from collections import Counter

def minimumLength(s: str) -> int:
    freq = Counter(s)
    for c in s:
        while freq[c]>2:
            freq[c]-=2
    return sum(freq.values())


s = "abaacbcbb"
print(minimumLength(s))