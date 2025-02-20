from functools import lru_cache
def numTilePossibilities(tiles: str) -> int:
    comb = set()
    @lru_cache(maxsize=None)
    def backtrack(pref, letters):
        for i in range(len(letters)):
            comb.add(pref + letters[i])
            backtrack(pref + letters[i], letters[:i] + letters[i + 1:])
    backtrack("", tiles)
    return len(comb)
tiles = "V"
print(numTilePossibilities(tiles))