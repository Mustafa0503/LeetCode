class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        memo = [[-1 for _ in range(amount+1)] for __ in range(len(coins)+1)]

        def dfs(i, target):

            if target>amount or i>=len(coins):
                return 0

            if memo[i][target]!=-1:
                return memo[i][target]

            if target == amount:
                return 1

            take = dfs(i, target+coins[i])
         
            skip = dfs(i+1, target)

            memo[i][target] = take+skip
            return take+skip
        
        res = dfs(0, 0)
        return res