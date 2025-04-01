def numberOfSubstrings(s: str) -> int:
    def _has_all_char():
        return all(f for f in freq)

    n = len(s)
    freq = [0]*3
    left=right=0

    out = 0

    while right<n:
        freq[ord(s[right])-ord('a')]+=1

        while _has_all_char():
           out+=n-right
           freq[ord(s[left]) - ord('a')] -= 1
           left += 1

        right+=1

    return out

s = "abcabc"
print(numberOfSubstrings(s))