def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix[j][n - 1 - i] + matrix[i][j]
            matrix[i][j] = matrix[i][j] - matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[j][n - 1 - i] - matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)