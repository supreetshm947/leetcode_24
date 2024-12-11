from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m=len(matrix)
    n=len(matrix[0])
    left=0
    right=m*n-1
    while left<=right:
        mid=(left+right)//2
        i=mid//n
        j=mid%n
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]<target:
            left=mid+1
        else:
            right=mid-1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
targets = [j for i in matrix for j in i]
for target in targets:
# target = 34
    print(searchMatrix(matrix, target))

print(searchMatrix(matrix, 55))