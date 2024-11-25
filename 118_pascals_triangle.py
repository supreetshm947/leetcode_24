def pascals_triangle(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    pascal = []
    for i in range(numRows):
        row = []
        if i == 0:
            row.append(1)
        else:
            for j in range(i+1):
                row.append(
                    (0 if j-1<0 else pascal[i-1][j-1]) + (pascal[i-1][j] if j<len(pascal[i-1]) else 0))
        pascal.append(row)

    return pascal

numRows = 5
print(pascals_triangle(numRows))