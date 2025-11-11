class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten =0
        good=0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good +=1
                if grid[i][j] == 2:
                    q.append((i,j))
        maxi = 0
        while(q and good>0):
            for _ in range(len(q)):
                row,col = q.popleft()
                if 0<row+1<len(grid) and grid[row+1][col]==1:
                    q.append((row+1,col))
                    grid[row+1][col] = 2
                    good-=1
                if 0<col+1<len(grid[0]) and grid[row][col+1]==1:
                    q.append((row,col+1))
                    grid[row][col+1] = 2
                    good-=1
                if 0<=col-1<len(grid[0]) and grid[row][col-1]==1:
                    q.append((row,col-1))
                    grid[row][col-1] = 2
                    good-=1
                if 0<=row-1<len(grid) and grid[row-1][col]==1:
                    q.append((row-1,col))
                    grid[row-1][col] = 2
                    good-=1
            maxi+=1
            
        if good==0:
            return maxi
        return -1
                        