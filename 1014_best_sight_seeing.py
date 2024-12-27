from typing import List

def maxScoreSightseeingPair(values: List[int]) -> int:
    max_left_score = values[0]
    max_sum = 0

    for i in range(1, len(values)):
        max_sum = max(max_sum, max_left_score + values[i] - i)
        max_left_score = max(max_left_score, values[i] + i)

    return max_sum

values = [1,2]
print(maxScoreSightseeingPair(values))