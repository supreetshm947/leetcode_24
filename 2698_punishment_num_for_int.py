from functools import lru_cache

def punishmentNumber(n: int) -> int:
    def can_partition(num, target):
        @lru_cache(maxsize=None)
        def backtrack(curr_sum, index):
            if index == len(num):
                return curr_sum == target
            n=0
            for j in range(index, len(num)):
                n=n*10+int(num[j])
                if n > target:
                    break
                if backtrack(curr_sum+n, j+1):
                    return True
            return False
        return backtrack(0, 0)

    out=0
    for i in range(1,n+1):
        sq = str(i*i)
        if can_partition(sq, i):
            out+=i*i
    return out

n = 37
print(punishmentNumber(n))