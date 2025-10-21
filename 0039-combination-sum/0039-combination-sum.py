class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        res  = []
        def dfs(i,curr):

            if curr==target:
                res.append(temp.copy())
                return
            if i>=len(candidates) or curr>target:
                return


            temp.append(candidates[i])
            dfs(i,sum(temp))

            temp.pop()
            dfs(i+1,sum(temp))
        dfs(0,0)
        return res
        