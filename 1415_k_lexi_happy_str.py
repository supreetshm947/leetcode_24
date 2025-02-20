def getHappyString(n: int, k: int) -> str:
    def backtrack(last_str):
        nonlocal count
        if len(last_str) == n:
            count+=1
            if count==k:
                return last_str
            return


        for c in "abc":
            if last_str and last_str[-1] == c:
                continue
            if out:=backtrack(last_str+c):
                return out

    count=0
    return backtrack("") or ""

n = 3
k = 9
print(getHappyString(n, k))