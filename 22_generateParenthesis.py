def generateParenthesis(n):
    def backtrack(current, open, close):
        # Base case: if the current string has reached the length 2 * n
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add an opening parenthesis if there are any left to add
        if open < n:
            backtrack(current + '(', open + 1, close)

        # Add a closing parenthesis if there are more open parentheses than close
        if close < open:
            backtrack(current + ')', open, close + 1)

    result = []
    backtrack("", 0, 0)  # Start with an empty string and 0 open and close parentheses
    return result


# Example usage:
n = 3
print(generateParenthesis(n))
# Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
