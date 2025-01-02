def maxScore(s: str) -> int:
    ones = 0
    for c in s:
        if c == '1':
            ones += 1
    zeroes=0
    ans=0
    for i in range(len(s)-1):
        if s[i]=='0':
            zeroes+=1
        else:
            ones-=1
        ans=max(ans,zeroes+ones)
    return ans

s = "0100111"
print(maxScore(s))