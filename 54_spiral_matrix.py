def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    out = []
    while matrix:
        out += matrix.pop(0)
        if matrix:
            matrix = [list(i) for i in zip(*matrix)][::-1]
    return out

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))