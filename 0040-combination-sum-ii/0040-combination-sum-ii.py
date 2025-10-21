class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        res  = []
        candidates.sort()
        def dfs(i,curr):

            if curr==target:
                
                res.append(sorted(temp).copy())
                return
            if i>=len(candidates) or curr>target:
                return


            temp.append(candidates[i])

            dfs(i+1,sum(temp))
            while(i+1<len(candidates) and candidates[i]==candidates[i+1]):
                i+=1
            temp.pop()
            dfs(i+1,sum(temp))
        dfs(0,0)
        return res