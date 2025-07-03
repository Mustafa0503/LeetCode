class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)+1
        cols = len(text2)+1
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        for r in range(len(text1)-1, -1, -1):
            for c in range(len(text2)-1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = dp[r+1][c+1] + 1
                else:
                    dp[r][c] = max(dp[r][c+1], dp[r+1][c])
        
        return dp[0][0]
            