from typing import List

def mostPoints(questions: List[List[int]]) -> int:
    n = len(questions)
    dp = [0]*(n+1)

    for i in range(n-1, -1, -1):
        points, power = questions[i]
        next_question = i+power+1

        solve = points + (dp[next_question] if next_question<n else 0 )

        skip = dp[i+1]

        dp[i] = max(solve, skip)

    return dp[0]

questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(mostPoints(questions))