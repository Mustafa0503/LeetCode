class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #lol
        return comb(m+n-2,m-1)