class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(),set()
        row, col = len(heights), len(heights[0])
        ans=[]

        def dfs(i,j,visit,prev):
            
            if(i<0 or j<0 or i>=row or j>=col or heights[i][j]<prev or (i,j) in visit):
               
                return
            print(i,j,heights[i][j],prev)
            visit.add((i,j))
            dfs(i+1,j,visit, heights[i][j])
            dfs(i-1,j,visit, heights[i][j])
            dfs(i,j+1,visit, heights[i][j])
            dfs(i,j-1,visit, heights[i][j])


        for i in range(row):
            dfs(i,0,pacific, heights[i][0])
        for i in range(col):
            dfs(0,i,pacific,heights[0][i])


        for i in range(row):
            dfs(i, col - 1, atlantic, heights[i][col - 1])
        for j in range(col):
            dfs(row - 1, j, atlantic, heights[row - 1][j])



        for i in range(row):
            for j in range(col):
                if (i,j) in atlantic and (i,j) in pacific:
                    
                    ans.append([i,j])
        return ans