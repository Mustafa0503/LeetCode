class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==1):
            return 0
        p1 = 0
        p2 = 1
        m=prices[p2]-prices[p1]
        for i in range(1,len(prices)):
            if(prices[p2]<=prices[i] or (prices[i]-prices[p1]>m and p1<i)):
                p2 = i
                m = max(m,prices[p2]-prices[p1])
            if(prices[p1]>prices[i]):
                p1 = i
                if(p2>p1):
                    m = max(m,prices[p2]-prices[p1])
        return max(m,0)


