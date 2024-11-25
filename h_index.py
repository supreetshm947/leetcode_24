def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    citations.sort()
    n = len(citations)
    h_ind = 0
    for i in range(n):
        if h_ind > n - i:
            break
        h_ind = min(citations[i], n - i)
    return h_ind