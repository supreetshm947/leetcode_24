from typing import List
from collections import Counter

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    d = Counter()
    for word in words2:
        word_count=Counter(word)
        for c in word_count:
            d[c]=max(d[c], word_count[c])

    result = []
    for word in words1:
        word_count=Counter(word)
        if all(word_count[c]>=d[c] for c in d):
            result.append(word)

    return result

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["l","e"]
print(wordSubsets(words1, words2))