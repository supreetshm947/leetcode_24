from typing import List

def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    n=len(s)
    all_shift=[0]*(n+1)
    for start,end, shift in shifts:
        c=-1 if not shift else 1
        all_shift[start]+=c
        all_shift[end+1]-=c
    ans = ""
    curr_shift=0
    for i in range(n):
        curr_shift+=all_shift[i]
        new_char = chr((ord(s[i])-ord('a')+curr_shift)%26+ord('a'))
        ans+=new_char
    return ans

s = "abc"
shifts =[[0,1,0],[1,2,1],[0,2,1]]
print(shiftingLetters(s, shifts))