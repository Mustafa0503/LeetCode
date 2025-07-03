class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        tooMuch = amount + 1
        dp = [tooMuch] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
        if dp[amount] == tooMuch:
            return -1
        else:
            return dp[amount]    