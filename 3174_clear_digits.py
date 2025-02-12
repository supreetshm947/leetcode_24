def clearDigits(s: str) -> str:
    stack = []
    for c in s:
        if 97<=ord(c)<=122:
            stack.append(c)
        elif stack:
            stack.pop()
    return ''.join(stack)



# s = "cb34"
s = "abc"
print(clearDigits(s))