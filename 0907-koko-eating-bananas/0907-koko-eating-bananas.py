class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(piles:List[int], hour: int):
            total = 0
            for i in piles:
                total = ceil(i/hour)+total

            return total
        l,r =1, max(piles)
        mid = (r-l)//2+l
        an=0
        while(l<=r):
            mid = (r-l)//2+l
            if(h<can(piles, mid)):
                l=mid+1
            else:
                r=mid-1
                an=mid
        return an