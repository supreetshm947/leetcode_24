from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n=len(temperatures)
    stack=[]
    output=[0]*n
    for i in range(n):
        while stack and temperatures[stack[-1]]<temperatures[i]:
            t=stack.pop()
            output[t]=i-t
        stack.append(i)
    return output

temperatures = [30,60,90]
print(dailyTemperatures(temperatures))
