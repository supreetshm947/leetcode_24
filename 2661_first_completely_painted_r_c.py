from typing import List

def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:
    m = len(mat)
    n = len(mat[0])

    num_to_index={}
    for i in range(m*n):
        num_to_index[arr[i]]=i

    last_elem_index=float("inf")

    for r in range(m):
        result = float("-inf")
        for c in range(n):
            result = max(num_to_index[mat[r][c]], result)
        last_elem_index = min(last_elem_index, result)

    for c in range(n):
        result = float("-inf")
        for r in range(m):
            result = max(num_to_index[mat[r][c]], result)
        last_elem_index = min(last_elem_index, result)

    return last_elem_index

arr = [2,8,7,4,1,3,5,6,9]
mat = [[3,2,5],[1,4,6],[8,7,9]]
print(firstCompleteIndex(arr, mat))