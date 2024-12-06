from collections import deque
def findLexSmallestString(s: str, a: int, b: int) -> str:
    def inc_odd(s, a):
        out = ""
        for i, c in enumerate(s):
            t = c
            if i % 2 == 1:
                t = str((int(c) + a) % 10)
            out += t
        return out

    def rotate(s, b):
        return  s[-b:]+s[:-b]

    q = deque([s])
    visited = {s}
    least = s
    while q:
        n = q.popleft()
        if least > n:
            least = n
        t = inc_odd(n, a)
        if t not in visited:
            visited.add(t)
            q.append(t)

        t = rotate(t, b)
        if t not in visited:
            visited.add(t)
            q.append(t)

    return least


s = "5525"
a = 9
b = 2
print(findLexSmallestString(s, a, b))