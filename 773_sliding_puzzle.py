from collections import deque

def slidingPuzzle(board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    # Applying BFS with board as the state at any given point

    target = (1, 2, 3, 4, 5, 0)

    board = tuple(sum(board, []))

    if target == board:
        return 0

    q = deque([(board, board.index(0), 0)])

    directions = [1, -1, 3, -3]
    visited = [board]

    while q:
        board, zero_index, move = q.popleft()

        for direction in directions:
            new_index = zero_index + direction

            if 0 <= new_index < 6 and (zero_index % 3 != 0 or direction != -1) and (
                    zero_index % 3 != 2 or direction != 1):
                new_board = list(board)
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                new_board = tuple(new_board)

                if new_board == target:
                    return move + 1

                if new_board not in visited:
                    visited.append(new_board)
                    q.append((new_board, new_index, move + 1))

    return -1

board = [[4,1,2],[5,0,3]]
print(slidingPuzzle(board))