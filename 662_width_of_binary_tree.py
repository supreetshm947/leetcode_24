from collections import deque

def widthOfBinaryTree( root):
    if not root:
        return 0

    max_width = 0
    queue = deque([(root, 0)])

    while queue:
        level_length = len(queue)
        _, level_start = queue[0]

        for i in range(level_length):
            node, index = queue.popleft()

            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))

        max_width = max(max_width, index - level_start + 1)

    return max_width

root = [1,3,2,5,3,None,9]
widthOfBinaryTree(root)