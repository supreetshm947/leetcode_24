# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        s = [root]
        while s:
            node = s.pop()
            if node:
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
                node.left=None
                node.right=right=s[-1] if s else None