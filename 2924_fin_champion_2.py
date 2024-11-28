class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        undef = [True] * n
        for w, l in edges:
            undef[l] = False

        if sum(undef) > 1:
            return -1
        return undef.index(True)