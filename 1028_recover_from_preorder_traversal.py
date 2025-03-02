from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.index = 0
        self.n = 0
        self.traversal = None

    def recurse(self, depth:int) -> TreeNode:
        if self.index >= self.n:
            return None
        dash_count = 0
        while self.index+dash_count < self.n and self.traversal[self.index+dash_count] == '-':
            dash_count += 1

        if dash_count != depth:
            return None

        self.index += dash_count

        value = 0
        while self.index < self.n and self.traversal[self.index].isdigit():
            value = value*10 + int(self.traversal[self.index])
            self.index += 1

        node = TreeNode(value)
        node.left = self.recurse(depth+1)
        node.right = self.recurse(depth+1)

        return node


    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.n = len(traversal)
        self.traversal = traversal
        return self.recurse(0)

sol = Solution()
ouy = sol.recoverFromPreorder("1-2--3--4-5--6--7")
print(ouy)