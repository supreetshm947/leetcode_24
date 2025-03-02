from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        def _construct_tree(pre_start, pre_end, post_start):
            if pre_start > pre_end:
                return None

            if pre_start == post_start:
                return TreeNode(preorder[pre_start])

            left_root = preorder[pre_start+1]

            num_nodes_in_left = index_of_postorder[left_root]-post_start+1

            root = TreeNode(preorder[pre_start])
            root.left = _construct_tree(pre_start, pre_start+num_nodes_in_left, post_start)
            root.right = _construct_tree(pre_start+num_nodes_in_left, pre_end, post_start+num_nodes_in_left)

            return root

        index_of_postorder = [0]*(n+1)
        for i in range(n):
            index_of_postorder[postorder[i]] = i

        return _construct_tree(0, n-1, 0)

