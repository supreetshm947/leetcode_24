from typing import List

def evalRPN(tokens: List[str]) -> int:
    operators = ['+', '-', '*', '/']
    stack = []
    for token in tokens:
        if token not in operators:
            stack.append(token)
        else:
            stack.append(int(eval(f"{stack.pop(-2)}{token}{stack.pop(-1)}")))
    return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))