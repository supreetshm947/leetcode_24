def getSmallestString(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    n = len(s)
    res = ""
    for i in range(n):
        t = ord(s[i])
        if k > 0:
            diff = min(t - ord('a'), ord('z') - t + 1)
            if k >= diff:
                k -= diff
                t = 97
            else:
                t -= k
                k = 0
        res += chr(t)
    return res

s = "zbbz"
k = 3
print(getSmallestString(s, k))