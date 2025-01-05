from collections import defaultdict

def countPalindromicSubsequence(s: str) -> int:
    dict = defaultdict(list)
    for i, c in enumerate(s):
        dict[c].append(i)
    ans=0
    for indices in dict.values():
        start=indices[0]
        end=indices[-1]
        seen=set()
        for i in range(start+1, end):
            seen.add(s[i])
        ans += len(seen)
    return ans

s = "aabca"
print(countPalindromicSubsequence(s))