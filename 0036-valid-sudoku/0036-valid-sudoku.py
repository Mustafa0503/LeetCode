class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setcol = set()
        setmid = set()
        setrow = set()
        for i in range(len(board)):
            for j in range(len(board)):
            

                if(i%3==0 and j%3==0):
                    
                    for o in range(i,i+3):
                        for k in range(j,j+3):
                            if(board[o][k]!="."):
                                if(board[o][k] in setmid):
                                    return False
                                else:
                                    setmid.add(board[o][k])
                    print(setmid)
                    setmid = set()
                if(board[i][j]!="."):
                    if(board[i][j] in setrow):
                        return False
                    else:
                        setrow.add(board[i][j])
                if(board[j][i]!="."):
                    if(board[j][i] in setcol):
                        return False
                    else:
                        setcol.add(board[j][i])
            
            setcol = set()
            setrow = set()

        return True
    board = [
    ["5", "3", "6", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],]
    print(isValidSudoku(0, board))