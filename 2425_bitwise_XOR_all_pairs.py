from typing import List

def xorAllNums(nums1: List[int], nums2: List[int]) -> int:
    len1 = len(nums1)
    len2 = len(nums2)

    freq = {}

    # [a,b], [c, d] = (a^c)^(a^d)^(b^c)^(b^d) = (a^a)^(b^b)^(c^c)^(d^d) - XOR is communicative
    # also a^a = 0 but a^a^a = a - so look for odd frequencies

    for i in nums1:
        freq[i] = freq.get(i, 0) + len2

    for i in nums2:
        freq[i] = freq.get(i, 0) - len1

    # a^0 = a
    ans = 0

    for f in freq:
        if freq[f] % 2:
            ans^=f

    return ans


nums1 = [2,1,3]
nums2 = [10,2,5,0]
print(xorAllNums(nums1, nums2))