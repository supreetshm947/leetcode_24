from bisect import bisect_right
from typing import List

def leftmostBuildingQueries(heights: List[int], queries: List[List[int]]) -> List[int]:

    result = [-1] * len(queries)
    # Stores the new queries for each building
    new_queries = [[] for _ in range(len(heights))]
    # Monotonic stack to keep the leftmost valid building
    mono_stack = []

    def binary_search(height: int, mono_stack: List[tuple]) -> int:
        # Binary search in the monotonic stack to find the highest possible position
        left, right = 0, len(mono_stack) - 1
        best_pos = -1
        while left <= right:
            mid = (left + right) // 2
            if mono_stack[mid][0] > height:
                best_pos = mid
                left = mid + 1
            else:
                right = mid - 1
        return best_pos

    # Preprocess the queries
    for i, (a, b) in enumerate(queries):
        if a > b:
            a, b = b, a  # Swap if a > b (ensuring a < b)
        # Direct answer if the height at b is greater than a or they are the same
        if heights[b] > heights[a] or a == b:
            result[i] = b
        else:
            new_queries[b].append((heights[a], i))

    # Process buildings from right to left
    for i in range(len(heights) - 1, -1, -1):
        # For each query at the current building i, check the conditions
        for height_a, idx in new_queries[i]:
            # Perform binary search to find the appropriate building
            pos = binary_search(height_a, mono_stack)
            if pos != -1:
                result[idx] = mono_stack[pos][1]

        # Maintain the monotonic stack where heights are strictly increasing
        while mono_stack and mono_stack[-1][0] <= heights[i]:
            mono_stack.pop()
        mono_stack.append((heights[i], i))

    return result




# Example usage
heights = [6, 4, 8, 5, 2, 7]
queries = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
print(leftmostBuildingQueries(heights, queries))
