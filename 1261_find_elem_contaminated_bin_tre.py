from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.elements = {0}
        root.val=0
        d = deque([root])
        while d:
            n = d.popleft()
            if n.left:
                n.left.val=2*n.val+1
                self.elements.add(n.left.val)
                d.append(n.left)
            if n.right:
                n.right.val=2*n.val+2
                self.elements.add(n.right.val)
                d.append(n.right)


    def find(self, target: int) -> bool:
        return target in self.elements
# Your FindElements object will be instantiated and called as such:
# [-1, null, -1], [1],[3],[5]
root = TreeNode(-1, TreeNode(None), TreeNode(-1))
obj = FindElements(root)

print(obj.find(1))
print(obj.find(2))
print(obj.find(5))