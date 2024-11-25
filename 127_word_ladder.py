from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    if endWord not in wordList:
        return 0

    length = len(beginWord)
    patterns = defaultdict(list)
    for word in wordList:
        for i in range(length):
            pattern = word[:i] + "_" + word[i + 1:]
            patterns[pattern].append(word)

    q = deque([[beginWord, 1]])
    visited = [beginWord]
    while q:
        word, depth = q.popleft()

        for i in range(length):
            w = word[:i] + "_" + word[i + 1:]
            for neighbor in patterns[w]:
                if neighbor == endWord:
                    return depth + 1
                elif neighbor not in visited:
                    q.append([neighbor, depth + 1])
                    visited.append(neighbor)
            patterns[w] = []

beginWord = "hit"
endWord = "cog"

wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))