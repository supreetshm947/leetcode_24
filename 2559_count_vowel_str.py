from typing import List

def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    n=len(words)
    pref_sum = [0]*n
    vowels = {'a', 'e', 'i', 'o','u'}
    for i in range(n):
        pref_sum[i]=pref_sum[i-1]+int(words[i][0] in vowels and words[i][-1] in vowels)
    ans = []
    for q in queries:
        if q[0] == 0:
            ans.append(pref_sum[q[1]])
        else:
            ans.append(pref_sum[q[1]]-pref_sum[q[0]-1])
    return ans

words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]
print(vowelStrings(words, queries))