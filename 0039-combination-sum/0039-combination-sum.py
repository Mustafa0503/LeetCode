class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        res  = []
        def dfs(i):

            if sum(temp)==target:
                res.append(temp.copy())
                return
            if i>=len(candidates):
                return
            if sum(temp)>target:
                return

            temp.append(candidates[i])
            dfs(i)

            temp.pop()
            dfs(i+1)
        dfs(0)
        return res
        