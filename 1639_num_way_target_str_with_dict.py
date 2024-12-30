from typing import List

def numWays(words: List[str], target: str) -> int:
    MOD = 10 ** 9 + 7
    m, n = len(target), len(words[0])
    dp = [[-1]*m for _ in range(n)]
    freq = [[0] * 26 for _ in range(n)]
    for word in words:
        for i, char in enumerate(word):
            freq[i][ord(char) - ord('a')] += 1

    def count_words(word_index, target_index):
        if target_index==m:
            return 1
        if word_index==n:
            return 0
        if dp[word_index][target_index] != -1:
            return dp[word_index][target_index]
        count_ways=0
        cur_pos=ord(target[target_index])-ord('a')
        count_ways+=freq[word_index][cur_pos]*count_words(word_index+1, target_index+1)
        count_ways+=count_words(word_index+1, target_index)
        dp[word_index][target_index] = count_ways%MOD

        return dp[word_index][target_index]

    return count_words(0, 0)



words = ["cbabddddbc","addbaacbbd","cccbacdccd","cdcaccacac","dddbacabbd","bdbdadbccb","ddadbacddd","bbccdddadd","dcabaccbbd","ddddcddadc","bdcaaaabdd","adacdcdcdd","cbaaadbdbb","bccbabcbab","accbdccadd","dcccaaddbc","cccccacabd","acacdbcbbc","dbbdbaccca","bdbddbddda","daabadbacb","baccdbaada","ccbabaabcb","dcaabccbbb","bcadddaacc","acddbbdccb","adbddbadab","dbbcdcbcdd","ddbabbadbb","bccbcbbbab","dabbbdbbcb","dacdabadbb","addcbbabab","bcbbccadda","abbcacadac","ccdadcaada","bcacdbccdb"]
target = "bcbbcccc"
print(numWays(words, target))