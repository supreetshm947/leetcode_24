def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    n = len(ratings)
    out = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            out[i] += 1

    for j in range(n - 2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            out[j] = max(out[j], out[j + 1] + 1)

    return sum(out)

ratings = [1,2,87,87,87,2,1]
print(candy(ratings))