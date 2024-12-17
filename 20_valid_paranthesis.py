def isValid(s: str) -> bool:
    paran_map = {
        '(':')',
        '{':'}',
        '[':']'
    }
    my_stack=[]
    for i in s:
        if i in paran_map:
            my_stack.append(i)
        else:
            if my_stack:
                o=my_stack.pop()
                if i==paran_map[o]:
                    continue
            return False
    return not my_stack

s = ")"
print(isValid(s))