def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """

    def backtrack(arr, start):
        if len(arr) == k:
            result.append(arr)
            return
        for i in range(start, n + 1):
            backtrack(arr + [i], start + 1)
            start+=1

    result = []
    backtrack([], 1)
    return result
n= 3
k=3
print(combine(n,k))