class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        isPal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or isPal[i + 1][j - 1]):
                    isPal[i][j] = True
    
        res = []
        path = []
        def dfs(start):
            if start == n:
                res.append(path.copy())
                return
            for end in range(start, n):
                if isPal[start][end]:
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()
        dfs(0)
        return res