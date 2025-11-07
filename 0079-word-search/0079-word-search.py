class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        le = len(word)
        temp = []
        ind = 0

        def dfs(i,j,ind):
            if(ind == le):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0])or word[ind]!=board[i][j]:
                return False
            char = board[i][j]
            board[i][j] = '#'
            res = (dfs(i+1,j,ind+1)or dfs(i,j+1,ind+1)or dfs(i-1,j,ind+1)or dfs(i,j-1,ind+1))

            board[i][j]=char
            return res
        for x in range(len(board)):
            for y in range(len(board[x])):
                if dfs(x,y,0):
                    return True
        return False