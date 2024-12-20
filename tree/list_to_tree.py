from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(lst):
    if not lst:
        return None

    # Create the root of the tree
    root = TreeNode(lst[0])
    queue = deque([root])  # Use a queue for level-order insertion
    i = 1  # Start from the second element in the list

    while queue and i < len(lst):
        current = queue.popleft()

        # Assign the left child if available
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1

        # Assign the right child if available
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root
