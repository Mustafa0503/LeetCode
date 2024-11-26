class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        if(len(nums)==0):
            return 0
        count = 0
        ma = 1
        for i in nums:
            if(i-1 not in s):
                temp = i
                while(temp in s):
                    temp = temp+1
                    count+=1
                ma = max(count,ma)
                count = 0

        return ma
