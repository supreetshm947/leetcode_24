from typing import Optional
from tree.list_to_tree import list_to_tree
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverseOddLevels(root: Optional[TreeNode]) -> Optional[TreeNode]:
    q = deque([root])
    level = 0
    while q:
        curr_level = []
        n = len(q)
        for _ in range(n):
            n = q.popleft()
            if level % 2 == 1:
                curr_level.append(n)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        if level % 2 == 1:
            for i in range(len(curr_level) // 2):
                curr_level[i].val, curr_level[-i - 1].val = curr_level[-i - 1].val, curr_level[i].val
        level += 1
    return root

root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
root = list_to_tree(root)
print(reverseOddLevels(root))

