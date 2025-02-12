def removeOccurrences(s: str, part: str) -> str:
    while part in s:
        s = s.replace(part, "", 1)
    return s


s = "aabababa"
part = "aba"

# s = "axxxxyyyyb"
# part = "xy"
print(removeOccurrences(s,part))