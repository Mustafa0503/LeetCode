class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1 = [0] * n

        
        maxprofit = 0
        buy = prices[0]
        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i] - buy)
            dp1[i] = maxprofit
        
        dp2 = [0] * n
        maxprofit = 0
        sell = prices[-1]
        for i in range(n-2, -1, -1):
            if prices[i] > sell:
                sell = prices[i]
            else:
                maxprofit = max(maxprofit, sell-prices[i])
            dp2[i] = maxprofit
        
        maxprofit = dp1[-1]

        for i in range(1,n-1):
            maxprofit = max(maxprofit, dp1[i]+dp2[i])
        return maxprofit