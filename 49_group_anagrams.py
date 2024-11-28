def groupAnagrams( strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    map = dict()
    for i in strs:
        key = "".join(sorted(i))
        if key not in dict():
            map[key] = []
        map[key].append(i)

    return map.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))