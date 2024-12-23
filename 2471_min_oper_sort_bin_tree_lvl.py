from typing import Optional
from collections import deque
from tree.list_to_tree import list_to_tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def minimumOperations(root: Optional[TreeNode]) -> int:
    def min_swaps_to_sort(arr):
        n = len(arr)
        indexed_arr = list(enumerate(arr))  # [(index, value), ...]
        indexed_arr.sort(key=lambda x: x[1])  # Sort by value

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or indexed_arr[i][0] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = indexed_arr[j][0]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps

    q = deque([root])
    total_swaps = 0

    while q:
        level_size = len(q)
        level_values = []

        for _ in range(level_size):
            node = q.popleft()
            level_values.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        total_swaps += min_swaps_to_sort(level_values)

    return total_swaps

root =[1,2,3,4,5,6]
root = list_to_tree(root)
print(minimumOperations(root))