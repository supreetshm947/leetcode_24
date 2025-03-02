from typing import List

def numOfSubarrays(arr: List[int]) -> int:
    n = len(arr)
    MOD=1e9 + 7
    dp_odd = [0] * n
    dp_even = [0] * n

    arr = [i%2 for i in arr]

    if arr[-1]==1:
        dp_odd[-1] = 1
    else:
        dp_even[-1] = 1

    for i in range(n-2,-1,-1):
        if arr[i]==1:
            dp_odd[i] = (1 + dp_even[i+1])%MOD
            dp_even[i] = dp_odd[i+1]
        else:
            dp_even[i] = (1 + dp_even[i + 1]) % MOD
            dp_odd[i] = dp_odd[i + 1]

    count = 0
    for i in dp_odd:
        count += i
        count %= MOD

    return int(count)

arr = [1,2,3,4,5,6,7]
print(numOfSubarrays(arr))