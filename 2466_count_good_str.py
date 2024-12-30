from typing import List

def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    MOD = 10 ** 9 + 7
    def recurse(end):
        # if end == 0:
        #     return 1
        if dp[end] != -1:
            return dp[end]
        answer=0
        if end>=zero:
            answer+=recurse(end-zero)
        if end>=one:
            answer+=recurse(end-one)
        dp[end] = answer%MOD
        return dp[end]
        # return answer
    out=0
    dp = [-1]*(high+1)
    dp[0]=1
    for i in range(low, high+1):
        out+=recurse(i)
    return out%MOD

low = 1
high = 100000
zero = 1
one = 1
print(countGoodStrings(low, high, zero, one))