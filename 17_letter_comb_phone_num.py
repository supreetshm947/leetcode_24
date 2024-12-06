from typing import List
def letterCombinations(digits: str) -> List[str]:
    keypad = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    n = len(digits)

    out = []

    def backtrack(s, start):
        if len(s) == n:
            out.append(s)
            return
        for i in range(start, n):
            for c in keypad.get(digits[i]):
                backtrack(s+c, i + 1)

    backtrack("", 0)
    return out

digits = "255"
print(letterCombinations(digits))