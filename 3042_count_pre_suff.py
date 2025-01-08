from typing import List

def countPrefixSuffixPairs(words: List[str]) -> int:
    def isPrefixAndSuffix(str1, str2):
        return str2.startswith(str1) and str2.endswith(str1)
    ans=0
    for i in range(len(words)-1):
        for j in range(i+1,len(words)):
            ans += isPrefixAndSuffix(words[i], words[j])
    return ans


words = ["a","aba","ababa","aa"]
print(countPrefixSuffixPairs(words))